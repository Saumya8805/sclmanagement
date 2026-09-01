from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile, TeacherProfile



class TeacherRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()   # ✅ new field
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = TeacherProfile
        fields = ['subject']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email




class StudentRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()   # ✅ new field
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StudentProfile
        fields = ['roll_no']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


