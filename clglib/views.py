from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta, date
from django.core.mail import send_mail

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin/')
    return render(request, 'index.html')

def adminclick(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin/')
    return render(request, 'adminclick.html')

def studentclick(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin/')
    return render(request, 'studentclick.html')

def adminsignup(request):
    form=forms.UserForm()
    if request.method=='POST':
        form=forms.UserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'adminsignup.html',{'form':form})

def studentsignup(request):
    form1=forms.UserForm()
    form2=forms.StudentForm()
    if request.method=='POST':
        form1=forms.UserForm(request.POST)
        form2=forms.StudentForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request, 'studentsignup.html', {'form1':form1,'form2':form2})

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def afterlogin(request):
    if is_admin(request.user):
        return render(request, 'adminafterlogin.html')
    else:
        return render(request, 'studentafterlogin.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def addbook(request):
    form=forms.BookForm()
    if request.method=='POST':
        form=forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request, 'bookadded.html')
    return render(request, 'addbook.html', {'form':form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewbook(request):
    books=models.Book.objects.all()
    return render(request, 'viewbook.html', {'books':books})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewstudent(request):
    students=models.Student.objects.all()
    return render(request, 'viewstudent.html', {'students':students})

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    form=forms.ContactusForm()
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['Name']
            sender_email = form.cleaned_data['Email']

            Message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['Message'])
            send_mail('New Enquiry', Message, sender_email, ['poojasalapu@gmail.com'])

            return render(request, 'contactdone.html')
    return render(request, 'contactus.html', {'form': form})

@user_passes_test(is_admin)
def issuebook(request):
    form=forms.BorrowerForm()
    if request.method=='POST':
        form=forms.BorrowerForm(request.POST)
        if form.is_valid():
            obj=models.Borrower()
            obj.title=request.POST.get('title1')
            obj.save()
            return render(request, 'bookissued.html')
    return render(request, 'issuebook.html', {'form':form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewissuedbook(request):
    issuedbooks=models.Borrower.objects.all()
    li=[]
    for ib in issuedbooks:
        issue_date=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        return_date=str(ib.returndate.day)+'-'+str(ib.returndate.month)+'-'+str(ib.returndate.year)
        days=(date.today()-ib.issuedate.date())
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*1

        books=list(models.Book.objects.filter(title=ib.title))
        students=list(models.Student.objects.filter(regd_no=ib.regd_no))
        i=0
        for l in books:
            t=(students[i].get_name,students[i].regd_no,books[i].title,books[i].author,issue_date,return_date,fine)
            i=i+1
            li.append(t)

    return render(request,'viewissuedbook.html',{'li':li})

login_required(login_url='studentlogin')
def book_student(request):
    student=list(models.Student.objects.filter(user_id=request.user.id))
    issuedbook=models.Borrower.objects.filter(regd_no=student[0].regd_no)
    li1=[]
    li2=[]
    for ib in issuedbook:
        books=models.Book.objects.filter(title=ib.title)
        for book in books:
            t=(request.user,student[0].regd_no,student[0].branch,book.name,book.author)
            li1.append(t)
        issue_date=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        return_date=str(ib.returndate.day)+'-'+str(ib.returndate.month)+'-'+str(ib.returndate.year)
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*1
        t=(issue_date,return_date,fine)
        li2.append(t)
    return render(request,'book_student.html',{'li1':li1,'li2':li2})

@login_required
def logout(request):
    logout(request)
    return redirect('index')