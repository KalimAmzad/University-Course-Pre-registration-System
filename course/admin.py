from django.contrib import admin
from course.models import *

class CourseListAdmin(admin.ModelAdmin):
	list_display = ['course_code','course_title','contact_hour','credit_hour','prerequisite','semester']
	search_fields = ('course_code','course_title','semester')
	ordering = ['course_code']

admin.site.register(CourseList, CourseListAdmin)

class CompletedCouse1stAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_code','gpa','teacher_id','section','semester']
	search_fields = ('course_code','student_id','section','teacher_id','semester')
	ordering = ['student_id','gpa']

admin.site.register(CompletedCouse1, CompletedCouse1stAdmin)

class CompletedCouse2ndAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_code','gpa','teacher_id','section','semester']
	search_fields = ('course_code','student_id','section','teacher_id','semester')
	ordering = ['student_id','gpa']

admin.site.register(CompletedCouse2, CompletedCouse2ndAdmin)

class CompletedCouse3rdAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_code','gpa','teacher_id','section','semester']
	search_fields = ('course_code','student_id','section','teacher_id','semester')
	ordering = ['student_id','gpa']

admin.site.register(CompletedCouse3, CompletedCouse3rdAdmin)

class CompletedCouse4thAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_code','gpa','teacher_id','section','semester']
	search_fields = ('course_code','student_id','section','teacher_id','semester')
	ordering = ['student_id','gpa']

admin.site.register(CompletedCouse4, CompletedCouse4thAdmin)

class CompletedCouse5thAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_code','gpa','teacher_id','section','semester']
	search_fields = ('course_code','student_id','section','teacher_id','semester')
	ordering = ['student_id','gpa']

admin.site.register(CompletedCouse5, CompletedCouse5thAdmin)

class CompletedCouse6thAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_code','gpa','teacher_id','section','semester']
	search_fields = ('course_code','student_id','section','teacher_id','semester')
	ordering = ['student_id','gpa']

admin.site.register(CompletedCouse6, CompletedCouse6thAdmin)

class CompletedCouse7thAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_code','gpa','teacher_id','section','semester']
	search_fields = ('course_code','student_id','section','teacher_id','semester')
	ordering = ['student_id','gpa']

admin.site.register(CompletedCouse7, CompletedCouse7thAdmin)

class CompletedCouse8thAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_code','gpa','teacher_id','section','semester']
	search_fields = ('course_code','student_id','section','teacher_id','semester')
	ordering = ['student_id','gpa']

admin.site.register(CompletedCouse8, CompletedCouse8thAdmin)

class ApplyingCourseAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_code','status','teacher_id','section','semester']
	search_fields = ('course_code','student_id','section','teacher_id')
	ordering = ['student_id']

admin.site.register(ApplyingCourse,ApplyingCourseAdmin)

class TakenCourseAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_code','status','teacher_id','section','gpa','semester']
	search_fields = ('course_code__course_code','student_id__user__username')
	ordering = ['student_id','gpa',]


admin.site.register(TakenCourse,TakenCourseAdmin)

admin.site.register(SemesterSelection)