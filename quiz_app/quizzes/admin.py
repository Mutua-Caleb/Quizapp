from django.contrib import admin
from .models import StudentUser, Category, Question 

admin.site.register(StudentUser)
admin.site.register(Category)
admin.site.register(Question)

# Register your models here.
