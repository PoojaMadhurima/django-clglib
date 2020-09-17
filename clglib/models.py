from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    regd_no = models.CharField(max_length=10)
    choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('Prefer not to say', 'Prefer not to say'),
    ]
    gender=models.CharField(max_length=20, choices=choices, default='none')
    options=[
        ('Computer Science & Engineering (CSE)', 'Computer Science & Engineering (CSE)'),
        ('Electronics & Communication Engineering (ECE)', 'Electronics & Communication Engineering (ECE)'),
        ('Electrical and Electronics Engineering (EEE)', 'Electrical and Electronics Engineering (EEE)'),
        ('Mechanical Engineering (ME)', 'Mechanical Engineering (ME)'),
        ('Civil Engineering (CE)', 'Civil Engineering (CE)'),
        ('Chemical Engineering (ChE)', 'Chemical Engineering (ChE)'),
        ('Master of Business Administration (MBA)', 'Master of Business Administration (MBA)'),
    ]
    branch=models.CharField(max_length=50, choices=options, default='none')
    contact_no = models.CharField(max_length=10)
    email_id=models.EmailField(unique=True)
    profile_image=models.ImageField(blank=True, upload_to='profile_image')
    bio = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user.first_name+'['+str(self.regd_no)+']'

    @property
    def get_name(self):
        return self.user.first_name

    @property
    def getuserid(self):
        return self.user.id

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    total_copies = models.IntegerField(default=1000)
    available_copies = models.IntegerField(default=1000)
    book_image=models.ImageField(blank=True, null=True, upload_to='book_image')

    @property
    def get_absolute_url(self):
        return str(self.title)

def get_expiry():
        return datetime.today() + timedelta(days=15)
class Borrower(models.Model):
    regd_no = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    issuedate = models.DateTimeField(auto_now=True)
    returndate = models.DateTimeField(default=get_expiry)

    def __str__(self):
        return self.regd_no



