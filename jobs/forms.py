from django import forms
from .models import Job
from companies.models import Company


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'company',
            'title',
            'description',
            'requirements',
            'location',
            'salary',
            'job_type',
            'experience_required',
            'deadline'
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter job title'}
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter job description',
                    'rows': 5
                }
            ),

            'requirements': forms.Textarea(
                attrs={
                    'placeholder': 'Enter job requirements',
                    'rows': 5
                }
            ),

            'location': forms.TextInput(
                attrs={'placeholder': 'Enter job location'}
            ),

            'salary': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter salary',
                    'min': 0
                }
            ),

            'experience_required': forms.NumberInput(
                attrs={
                    'placeholder': 'Years of experience required',
                    'min': 0
                }
            ),

            'deadline': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class JobSearchForm(forms.Form):

    q = forms.CharField(
        required=False,
        label='Search',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search job title, skills or keywords'
            }
        )
    )

    location = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter location'
            }
        )
    )

    job_type = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'All Job Types'),
            ('full_time', 'Full Time'),
            ('part_time', 'Part Time'),
            ('internship', 'Internship'),
            ('contract', 'Contract'),
        ]
    )

    company = forms.ModelChoiceField(
        required=False,
        queryset=Company.objects.all(),
        empty_label='All Companies'
    )