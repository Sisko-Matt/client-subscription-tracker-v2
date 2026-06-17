from django import forms
from .models import Client, Subscription

class ClientForm(forms.ModelForm):
    class Meta:

        model= Client
        fields= '__all__'

class SubscriptionForm(forms.ModelForm):
    class Meta:

        model= Subscription
        fields= '__all__'


