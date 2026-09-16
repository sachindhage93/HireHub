from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )

    user_type = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove username help text
        self.fields['username'].help_text = ''

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'This email is already registered.'
            )

        return email

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(
                    'Passwords do not match.'
                )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        # Password ko securely hash karega
        user.set_password(
            self.cleaned_data['password']
        )

        if commit:
            user.save()

            # User ka Profile create karega
            Profile.objects.create(
                user=user,
                user_type=self.cleaned_data['user_type']
            )

        return user