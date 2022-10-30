from django import forms
from django.core.validators import ValidationError
from django.contrib.auth import authenticate, get_user_model
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms.widgets import NumberInput
from .models import Booking, Product, Physiotherapist, Session, Price
from django.contrib.admin import widgets
import datetime

User = get_user_model()


class Loginform(forms.Form):
    username = forms.CharField(label="Nazwa użytkownika")
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)

    def clean(self):
        cd = super().clean()

        username = cd.get('username')
        password = cd.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            raise ValidationError("Złe podane hasło lub login")


class Registerform(forms.ModelForm):
    pass1 = forms.CharField(label="Hasło", widget=forms.PasswordInput)
    pass2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )
        help_texts = {
            'username': 'Tym będziesz się logował',
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Ta nazwa użytkownika już istnieje")
        return username

    def clean(self):
        cd = super().clean()
        pass1 = cd.get('pass1')
        pass2 = cd.get('pass2')
        if len(pass1) < 4:
            raise ValidationError('Hasło musi mieć więcej niż 4 litery!')
        if pass1 != pass2:
            raise ValidationError('Hasło musi być takie same')


class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("physiotherapist", "product", "session", "price", "date")
        widgets = {
            'date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
            })
        }
        labels = {
            "physiotherapist": "Specjalista",
            "product": "Usługa",
            "session": "Sesja",
            "price": "Cena",
            "date": "Data",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.none()
        self.fields['session'].queryset = Session.objects.none()
        self.fields['price'].queryset = Price.objects.none()

        if 'physiotherapist' in self.data:
            try:
                physiotherapist_id = int(self.data.get('physiotherapist'))
                self.fields['product'].queryset = Product.objects.filter(physiotherapist_id=physiotherapist_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['product'].queryset = self.instance.physiotherapist.product_set

        if 'product' in self.data:
            try:
                product_id = int(self.data.get('product'))
                self.fields['session'].queryset = Session.objects.filter(product_id=product_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['session'].queryset = self.instance.product.session_set

        if 'session' in self.data:
            try:
                session_id = int(self.data.get('session'))
                self.fields['price'].queryset = Price.objects.filter(session_id=session_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['price'].queryset = self.instance.session.price_set
