from .models import Client
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm, SubscriptionForm
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from .models import Subscription
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
    status_filter = request.GET.get('status')
    today = timezone.now().date()

    subscriptions = Subscription.objects.all()

    filter_type = request.GET.get('filter')

    if filter_type == 'active':

        subscriptions = subscriptions.filter(
            expiry_date__gte=today
        )

    elif filter_type == 'expired':

        subscriptions = subscriptions.filter(
            expiry_date__lt=today
        )

    elif filter_type == 'expiring':

        subscriptions = subscriptions.filter(
            expiry_date__gte=today,
            expiry_date__lte=next_7_days
        )

    elif filter_type == 'paid':

        subscriptions = subscriptions.filter(
            payment_status='paid'
        )

    elif filter_type == 'unpaid':

        subscriptions = subscriptions.filter(
            payment_status='unpaid'
        )

    return render(request, 'tracker/subscription_list.html', {
        'subscriptions': subscriptions,
        'status_filter': status_filter,
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

def login_view(request):

    error = None

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        else:

            error = "Invalid username or password."

    return render(
        request,
        'tracker/login.html',
        {
            'error': error
        }
    )

def logout_view(request):

    messages.info(
        request,
        "You have been logged out successfully."
    )

    logout(request)

    return redirect('login')