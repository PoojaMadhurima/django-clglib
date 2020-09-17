from django import forms
from django.contrib.auth.models import User
from . import models

class AdminSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['regd_no', 'branch']

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['title', 'author', 'summary']

class BorrowerForm(forms.Form):
    title1=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="none", to_field_name="title",label='Title')
    regd_no1=forms.ModelChoiceField(queryset=models.Student.objects.all(),empty_label="none",to_field_name='regd_no',label='Registration Number')
    
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 2, 'cols': 30}))
