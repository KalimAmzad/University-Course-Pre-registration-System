from django.contrib import admin
from .models import StudentProfile, TeacherProfile

from course.models import TakenCourse

class TakenCourseAdmin(admin.TabularInline):
	model = TakenCourse
	extra = 1

class StudentProfileAdmin(admin.ModelAdmin):
	inlines = (TakenCourseAdmin,)
	list_display = ['user','email','mobile', 'sex','address','section','semester']

admin.site.register(StudentProfile, StudentProfileAdmin)

class TeacherProfileAdmin(admin.ModelAdmin):
	list_display = ['user','email','mobile','address']

admin.site.register(TeacherProfile, TeacherProfileAdmin)