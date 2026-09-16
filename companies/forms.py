from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company

        fields = [
            'name',
            'description',
            'website',
            'location',
            'logo',
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter company name'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter company description',
                    'rows': 5
                }
            ),

            'website': forms.URLInput(
                attrs={
                    'placeholder': 'https://example.com'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Enter company location'
                }
            ),
        }