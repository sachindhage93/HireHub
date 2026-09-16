from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            'phone',
            'location',
            'skills',
            'experience',
            'resume',
            'profile_picture',
        ]

        widgets = {

            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Enter phone number'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your location'
                }
            ),

            'skills': forms.Textarea(
                attrs={
                    'placeholder': 'Enter your skills',
                    'rows': 4
                }
            ),

            'experience': forms.NumberInput(
                attrs={
                    'placeholder': 'Years of experience',
                    'min': 0
                }
            ),

        }