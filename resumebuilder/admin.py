from django.contrib import admin
from .models import Profile

#model register
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'gender',
        'title',
        'address',
        'email',
        'social',
        'number',
        'objective',
        'company_name',
        'job_title',
        'job_works',
        'job_date_from',
        'job_date_to',
        'college_name',
        'course',
        'course_modules',
        'gpa',
        'skills',
        'profile_picture')