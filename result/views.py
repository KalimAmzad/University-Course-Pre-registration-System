from django.shortcuts import render,redirect
from django.http import Http404, HttpResponseNotFound 
from django.contrib.admin.views.decorators import staff_member_required

import csv
from django.core.files.storage import FileSystemStorage
from account.models import StudentProfile,TeacherProfile
from course.models import *
from .models import *
from .forms import ResultForm

@staff_member_required
def upload_result(request):
	user  = request.user
	teacher_id = user.username
	print(teacher_id)

	if request.method == 'POST' and  request.FILES['result']:

		course = request.POST.get("course")
		section = request.POST.get("section")

		result_file = request.FILES['result']
		fs = FileSystemStorage()
		filename = fs.save(result_file.name, result_file)
		uploaded_file_url = fs.url(filename)
		prev = "C:/Users/Parents/Desktop/MyEnv_2.0/pre_registration"+uploaded_file_url
		print(prev)
		data = csv.reader(open(prev),delimiter=",")

		for row in data:

			if (row[0] != 'Student_id'): 
				return HttpResponseNotFound("<h1>Your CSV file format is not correct.Make sure that 1st row title is 'student_id'. Try again please.<h1>")
			else:
				break	
		
		for row in data:
			if float(row[1]) >= 2.00:
				if section[0] == '1':
					result_upload = CompletedCouse1()
					result_upload_result = Result1()
				elif section[0] == '2':
					result_upload = CompletedCouse2()
					result_upload_result = Result2()
				elif section[0] == '3':
					result_upload = CompletedCouse3()
					result_upload_result = Result3()
				elif section[0] == '4':
					result_upload = CompletedCouse4()
					result_upload_result = Result4()
				elif section[0] == '5':
					result_upload = CompletedCouse5()
					result_upload_result = Result5()
				elif section[0] == '6':
					result_upload = CompletedCouse6()
					result_upload_result = Result6()
				elif section[0] == '7':
					result_upload = CompletedCouse7()
					result_upload_result = Result7()
				elif section[0] == '8':
					result_upload = CompletedCouse8()
					result_upload_result = Result8()

				course_obj = CourseList.objects.get(course_code=course)
				student_obj = StudentProfile.objects.get(user__username=row[0])
				teacher_obj = TeacherProfile.objects.get(user__username=teacher_id)
				new_semester = SemesterSelection.objects.all()[0]
				new_semester = str(new_semester)
				if(new_semester[0:3]=='AUT' or new_semester[0:3]=='aut' or new_semester[0:3]=='Aut'):
					sem = 'SP'
					prev_sem = sem + ' - ' +str(int(new_semester[-2:]))
				else:
					sem = 'AUT'
					prev_sem = sem + ' - ' +str(int(new_semester[-2:])-1)
				print(prev_sem)
				taken_course_insert = TakenCourse.objects.get(student_id=student_obj,
						course_code=course_obj,semester=prev_sem)
				
				
				result_upload.student_id = student_obj
				result_upload.gpa = row[1]
				result_upload.teacher_id = teacher_obj
				result_upload.section = section
				result_upload.course_code = course_obj
				result_upload.semester  = prev_sem
				result_upload.save()

				result_upload_result.student_id = student_obj
				result_upload_result.course_id = course_obj
				result_upload_result.gpa = row[1]
				result_upload_result.save()

				taken_course_insert.gpa = row[1]
				taken_course_insert.save()

				update_section = str(int(section[0])+1) + section[-2:]
				taken = TakenCourse.objects.filter(student_id=student_obj,semester=new_semester)[0]
				next_section = taken.section

				if update_section == next_section:
					student_obj.section = update_section
				student_obj.semester = int(section[0])+1
				student_obj.save()

				

		print(course,section,uploaded_file_url)
		return HttpResponseNotFound("<h1>Successfully sumbitted.<h1>")
			


	return render(request, 'result/upload_result.html', {})




# def upload_result(request):
# 	user  = request.user
# 	teacher_id = user.username

# 	if request.method == 'POST':

# 		courses = request.POST.getlist("course")
# 		courses = list(filter(None, courses))
# 		sections = request.POST.getlist("section")
# 		sections = list(filter(None, sections))
# 		files = request.POST.getlist("file")
# 		files = list(filter(None, files))

# 		total = len(courses)

# 		print(courses, sections, files)

# 		for i in range(total):
# 			print(courses[i], sections[i], files[i])
# 			files = request.FILES.getlist("file")
# 			course_obj = CourseList.objects.get(course_code=courses[i])
# 			section = sections[i]
# 			f = open(files, 'r')  
# 			for line in f:  
# 				line =  line.split(';')
# 				if section[0]=='1':
# 					student_obj = StudentProfile.objects.get(user__username=line[0])
# 					insert_result = Result1.object.get_or_create(student_id=student_obj, course_id=course_obj, gpa=line[1])


# 			   # product = Product()  
# 			   # product.name = line[2] + '(' + line[1] + ')'  
# 			   # product.description = line[4]  
# 			   # product.price = '' #data is missing from file  
# 			   # product.save()  

# 			f.close() 

# 	iteration = range(1,6)
# 	return render(request, 'result/upload_result.html', {'iteration': iteration})	
