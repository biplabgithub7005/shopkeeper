from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer

        fields = ['name','password','email','mobile']
    name = forms.CharField(max_length=100,
                           label='',
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder':'Enter Name',
                                   'class':'form-control',

                               }
                           )
                           )

    password = forms.CharField(max_length=100,
                           label='',
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder': 'Enter Password',
                                   'class': 'form-control',

                               }
                           )
                           )
    email = forms.CharField(max_length=100,
                               label='',
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': 'Enter Email',
                                       'class': 'form-control',

                                   }
                               )
                               )

    mobile = forms.CharField(max_length=100,
                            label='',
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Enter Mobile',
                                    'class': 'form-control',

                                }
                            )
                            )


class ExampleForm(forms.Form):
    c = Customer.objects.all()
    OPTIONS = []
    for i in c:
        OPTIONS.append((i.name, i.name))

    office = forms.MultipleChoiceField(
        choices=OPTIONS,
        initial='0',
        widget=forms.SelectMultiple(),
        required=True,
        label='Office',
    )


# class CustomerLogin(forms.Form):
#     email =forms.EmailField(
#         max_length=100,
#         label='',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Enter Email',
#                 'class': 'form-control',
#
#             }
#         )
#     )
#
#     password = forms.CharField(max_length=100,
#                                label='',
#                                widget=forms.PasswordInput(
#                                    attrs={
#                                        'placeholder': 'Enter Password',
#                                        'class': 'form-control',
#
#                                    }
#                                )
#                                )