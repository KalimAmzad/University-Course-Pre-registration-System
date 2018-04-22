from django.contrib import admin

from section.models import *

class Section1AMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section1AM,Section1AMAdmin)

class Section1BMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section1BM,Section1BMAdmin)



class Section1CMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section1CM,Section1CMAdmin)

class Section1DMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section1DM,Section1DMAdmin)

class Section2AMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section2AM,Section2AMAdmin)

class Section2BMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section2BM,Section2BMAdmin)



class Section2CMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section2CM,Section2CMAdmin)

class Section2DMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section2DM,Section2DMAdmin)

class Section3AMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section3AM,Section3AMAdmin)

class Section3BMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section3BM,Section3BMAdmin)



class Section3CMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section3CM,Section3CMAdmin)

class Section3DMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section3DM,Section3DMAdmin)

class Section4AMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section4AM,Section4AMAdmin)

class Section4BMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section4BM,Section4BMAdmin)



class Section4CMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section4CM,Section4CMAdmin)

class Section4DMAdmin(admin.ModelAdmin):
	list_display = ['student_id','course_id','teacher_id','result','status','semester']
	search_fields = ['student_id','course_id','teacher_id']
	ordering = ['course_id']

admin.site.register(Section4DM,Section4DMAdmin)

# admin.site.register(Section1DM,Section1DMAdmin)

# class Section2AMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section2AM,Section2AMAdmin)

# class Section2BMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section2BM,Section2BMAdmin)

# class Section2CMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section2CM,Section2CMAdmin)

# class Section2DMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section2DM,Section2DMAdmin)

# class Section3AMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section3AM,Section3AMAdmin)

# class Section3BMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section3BM,Section3BMAdmin)

# class Section3CMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section3CM,Section3CMAdmin)

# class Section3DMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section3DM,Section3DMAdmin)

# class Section4AMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section4AM,Section4AMAdmin)

# class Section4BMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section4BM,Section4BMAdmin)

# class Section4CMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section4CM,Section4CMAdmin)

# class Section4DMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section4DM,Section4DMAdmin)

# class Section5AMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section5AM,Section5AMAdmin)

# class Section5BMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section5BM,Section5BMAdmin)

# class Section5CMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section5CM,Section5CMAdmin)

# class Section5DMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section5DM,Section5DMAdmin)

# class Section6AMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section6AM,Section6AMAdmin)

# class Section6BMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section6BM,Section6BMAdmin)

# class Section6CMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section6CM,Section6CMAdmin)

# class Section6DMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section6DM,Section6DMAdmin)

# class Section7AMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section7AM,Section7AMAdmin)

# class Section7BMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section7BM,Section7BMAdmin)

# class Section7CMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section7CM,Section7CMAdmin)

# class Section7DMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section7DM,Section7DMAdmin)

# class Section8AMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section8AM,Section8AMAdmin)

# class Section8BMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section8BM,Section8BMAdmin)

# class Section8CMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section8CM,Section8CMAdmin)

# class Section8DMAdmin(admin.ModelAdmin):
# 	list_display = ['student_id','course_id','teacher_id','result']
# 	search_fields = ['student_id','course_id','teacher_id']
# 	ordering = ['course_id']

# admin.site.register(Section8DM,Section8DMAdmin)
