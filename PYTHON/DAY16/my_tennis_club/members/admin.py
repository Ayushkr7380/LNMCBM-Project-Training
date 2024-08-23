from django.contrib import admin
from .models import Member,Student

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','joined_date')
admin.site.register(Member,MemberAdmin)

admin.site.register(Student)
