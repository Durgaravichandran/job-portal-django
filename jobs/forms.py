
from django import forms
from .models import Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job

        fields = [
            'title',
            'company',
            'description',
            'location',
            'salary',
            'experience',
            'skills',
            'job_type',
        ]

        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 6
            }),

            'skills': forms.TextInput(attrs={
                'placeholder': 'Python, SQL, Django, HTML'
            }),
        }