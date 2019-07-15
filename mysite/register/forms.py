from django import forms
from .models import Register
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

    CHOICES = (

        ("", "--Select Payment Type--"),
        ("credit", "Credit"),
        ("cash", "Cash"),
    )
    type = forms.ChoiceField(choices=CHOICES)

