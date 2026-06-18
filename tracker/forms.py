from django import forms
from .models import Client, Subscription


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['payment_status'].widget.attrs['class'] = 'form-select'

        self.fields['start_date'].widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )

        self.fields['expiry_date'].widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )

    def clean(self):

        cleaned_data = super().clean()

        start_date = cleaned_data.get('start_date')
        expiry_date = cleaned_data.get('expiry_date')

        if start_date and expiry_date:

            if expiry_date < start_date:

                raise forms.ValidationError(
                    "Expiry date cannot be before start date."
                )

        return cleaned_data