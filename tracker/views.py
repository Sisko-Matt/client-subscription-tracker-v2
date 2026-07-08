import csv
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from datetime import timedelta
from .forms import ClientForm, SubscriptionForm
from .models import Client, Subscription


@login_required
def client_list(request):
    search_query = request.GET.get('q', '')

    clients = Client.objects.all()

    if search_query:

        clients = clients.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone_number__icontains=search_query) |
            Q(business_name__icontains=search_query)
        )
    return render(request, 'tracker/client_list.html', {
    'clients': clients,
    'search_query': search_query,
})


@login_required
def add_client(request):

    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Client added successfully."
            )

            return redirect('client-list')

    else:
        form = ClientForm()

    return render(request, 'tracker/client_form.html', {
        'form': form
    })

@login_required
def export_subscriptions_csv(request):
    today = date.today()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="Subscriptions {today}.csv"'

    writer = csv.writer(response)

    writer.writerow([
        'Client',
        'Business',
        'Start Date',
        'Expiry Date',
        'Amount Paid',
        'Payment Status'
    ])

    subscriptions = Subscription.objects.select_related('client').all()

    for subscription in subscriptions:
        writer.writerow([
            subscription.client.name,
            subscription.client.business_name,
            subscription.start_date,
            subscription.expiry_date,
            subscription.amount_paid,
            subscription.payment_status
        ])

    return response


@login_required
def edit_client(request, pk):

    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':

        form = ClientForm(
            request.POST,
            instance=client
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Client updated successfully."
            )

            return redirect('client-list')

    else:

        form = ClientForm(instance=client)

    return render(
        request,
        'tracker/client_form.html',
        {'form': form}
    )


@login_required
def add_subscription(request):

    if request.method == "POST":

        form = SubscriptionForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Subscription added successfully."
            )

            return redirect('subscription-list')

    else:
        form = SubscriptionForm()

    return render(
        request,
        'tracker/subscription_form.html',
        {'form': form}
    )


@login_required
def subscription_list(request):

    today = timezone.now().date()
    next_7_days = today + timedelta(days=7)

    filter_type = request.GET.get('status')

    subscriptions = Subscription.objects.all()

    # 🔥 Apply filters based on dropdown selection
    if filter_type == 'active':
        subscriptions = subscriptions.filter(expiry_date__gte=today)

    elif filter_type == 'expired':
        subscriptions = subscriptions.filter(expiry_date__lt=today)

    elif filter_type == 'expiring':
        subscriptions = subscriptions.filter(
            expiry_date__gte=today,
            expiry_date__lte=next_7_days
        )

    elif filter_type == 'paid':
        subscriptions = subscriptions.filter(payment_status='paid')

    elif filter_type == 'unpaid':
        subscriptions = subscriptions.filter(payment_status='unpaid')

    # 🔥 Derived datasets (for dashboard-style sections if you still use them)
    active = Subscription.objects.filter(expiry_date__gte=today)

    expired = Subscription.objects.filter(expiry_date__lt=today)

    expiring_soon = Subscription.objects.filter(
        expiry_date__gte=today,
        expiry_date__lte=next_7_days
    )

    unpaid = Subscription.objects.filter(payment_status='unpaid')

    return render(request, 'tracker/subscription_list.html', {
        'subscriptions': subscriptions,
        'active': active,
        'expired': expired,
        'expiring_soon': expiring_soon,
        'unpaid': unpaid,
        'filter_type': filter_type,
    })

@login_required
def dashboard(request):

    today = timezone.now().date()
    next_7_days = today + timedelta(days=7)

    total_clients = Client.objects.count()

    active_subscriptions = Subscription.objects.filter(
        expiry_date__gte=today
    ).count()

    expired_subscriptions = Subscription.objects.filter(
        expiry_date__lt=today
    ).count()

    expiring_soon = Subscription.objects.filter(
        expiry_date__gte=today,
        expiry_date__lte=next_7_days
    ).count()

    unpaid_subscriptions = Subscription.objects.filter(
        payment_status='unpaid'
    ).count()

    context = {
        'total_clients': total_clients,
        'active_subscriptions': active_subscriptions,
        'expired_subscriptions': expired_subscriptions,
        'expiring_soon': expiring_soon,
        'unpaid_subscriptions': unpaid_subscriptions,
    }

    return render(request, 'tracker/dashboard.html', context)

from django.contrib import messages

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            messages.success(
                request,
                f"Login Success. Welcome back, {user.username}!"
            )

            return redirect('dashboard')

        else:
            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, 'tracker/login.html')

def logout_view(request):

    messages.info(
        request,
        "You have been logged out successfully."
    )

    logout(request)

    return redirect('login')