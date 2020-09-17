from django.contrib import admin

# Register your models here.
from .models import Book, Student, Borrower

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class BorrowerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Borrower, BorrowerAdmin)




