from django.contrib import admin
from bmi.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['FullName','Gender','height','Weight','BMI_Calculate']