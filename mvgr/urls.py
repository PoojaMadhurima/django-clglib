from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from clglib import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),

    path('', views.home),
    path('adminclick/', views.adminclick),
    path('studentclick/', views.studentclick),
    
    path('adminclick/adminsignup', views.adminsignup),
    path('studentclick/studentsignup', views.studentsignup),
    path('adminclick/adminlogin/', LoginView.as_view(template_name='adminlogin.html')),
    path('studentclick/studentlogin/', LoginView.as_view(template_name='studentlogin.html')),
    path('afterlogin/', views.afterlogin),
    path('afterlogin/logout/', LogoutView.as_view(template_name='index.html')),
    
    path('afterlogin/addbook/', views.addbook),
    path('afterlogin/viewbook/', views.viewbook),
    path('afterlogin/issuebook/', views.issuebook),
    path('afterlogin/viewissuedbook/', views.viewissuedbook),
    path('afterlogin/book_student/', views.book_student),
    path('afterlogin/viewstudent/', views.viewstudent),

    path('aboutus/', views.aboutus),
    path('contactus/', views.contactus),
]

