from django.contrib import admin

from result.models import *


class Result1stAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','gpa',]
	search_fields = ['student_id','course_id',]
	ordering = ['student_id','gpa',]

admin.site.register(Result1,Result1stAdmin)

class Result2ndAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','gpa',]
	search_fields = ['student_id','course_id',]
	ordering = ['student_id','gpa',]

admin.site.register(Result2,Result2ndAdmin)

class Result3rdAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','gpa',]
	search_fields = ['student_id','course_id',]
	ordering = ['student_id','gpa',]

admin.site.register(Result3,Result3rdAdmin)

class Result4thAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','gpa',]
	search_fields = ['student_id','course_id',]
	ordering = ['student_id','gpa',]

admin.site.register(Result4,Result4thAdmin)

class Result5thAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','gpa',]
	search_fields = ['student_id','course_id',]
	ordering = ['student_id','gpa',]

admin.site.register(Result5,Result5thAdmin)

class Result6thAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','gpa',]
	search_fields = ['student_id','course_id',]
	ordering = ['student_id','gpa',]

admin.site.register(Result6,Result6thAdmin)

class Result7thAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','gpa',]
	search_fields = ['student_id','course_id',]
	ordering = ['student_id','gpa',]

admin.site.register(Result7,Result7thAdmin)

class Result8thAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','gpa',]
	search_fields = ['student_id','course_id',]
	ordering = ['student_id','gpa',]

admin.site.register(Result8,Result8thAdmin)	
