from django.contrib import admin
from singup.models import Member
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['Email','password','firstname','lastname']