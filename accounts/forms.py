from django import forms
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    user_type = forms.ChoiceField(
        choices=Profile.USER_TYPES
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data['password']
        )

        if commit:
            user.save()

            Profile.objects.create(
                user=user,
                user_type=self.cleaned_data['user_type']
            )

        return user


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            'phone',
            'skills',
            'education',
            'experience',
            'resume'
        ]

        widgets = {
            'skills': forms.TextInput(
                attrs={
                    'placeholder': 'Python, SQL, Django, HTML'
                }
            ),

            'education': forms.TextInput(
                attrs={
                    'placeholder': 'B.E Computer Science'
                }
            ),

            'experience': forms.TextInput(
                attrs={
                    'placeholder': 'Fresher / 1 year'
                }
            ),
        }