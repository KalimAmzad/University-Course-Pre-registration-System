from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from course.models import *
from account.models import StudentProfile
from section.models import *


@login_required
def pre_registration(request):

	user = request.user
	student = StudentProfile.objects.get(user=user)
	current_semester = SemesterSelection.objects.all()[0]
	new_semester = current_semester.semester
	print(new_semester)

	if(new_semester[0:3]=='AUT' or new_semester[0:3]=='aut' or new_semester[0:3]=='Aut'):
		sem = 'SP'
		prev_sem = sem + ' - ' + str(int(new_semester[-2:]))
		prev_prev_sem = 'AUT - '
	else:
		sem = 'AUT'
		prev_sem = sem + ' - ' + str(int(new_semester[-2:])-1)
		prev_prev_sem = 'SP - '
	prev_prev_sem = prev_prev_sem + str(int(new_semester[-2:])-1)
	print(prev_sem,prev_prev_sem)

	if request.method == 'POST':

		taken = request.POST.getlist("course")
		prefer_section = request.POST.getlist("prefer_section")
		prefer_section = list(filter(None, prefer_section))
		print(prefer_section)
		course_list = []
		index = 0
		for course in taken:
			course_obj = CourseList.objects.get(course_code=course)
			course_list += [course_obj]
			semester = course_obj.semester
			semester = int(semester)
			student_obj = StudentProfile.objects.get(user=user)
			currect_section = student_obj.section

			next_section_no = int(currect_section[0]) + 1

			if currect_section[0] == '1' and semester == 1:
				insert_course = TakenCourse.objects.get_or_create(student_id=student_obj,
				course_code = course_obj, status='REGULAR',semester=prev_sem, section=currect_section)
				insert_course_section = section_insert(student_obj, course_obj, prev_sem, currect_section)

			elif semester == next_section_no:
				next_section = str(next_section_no)+currect_section[-2:]
				print(next_section, course_obj.id)

				# also insert this course to the section
				insert_course = TakenCourse.objects.get_or_create(student_id=student_obj,
				course_code = course_obj, status='REGULAR',semester=new_semester, section=next_section)
				insert_course_section = section_insert(student_obj, course_obj, new_semester, next_section)
			else:
				insert_course = ApplyingCourse.objects.get_or_create(student_id=student_obj,
				course_code = course_obj, status='IRREGULAR',semester=new_semester,section=prefer_section[index])
				index = index+1


	

	student_obj = StudentProfile.objects.get(user=user)
	currect_section = student_obj.section
	print(currect_section)

	next_section_no = int(str(currect_section)[0]) + 1
	next_section = str(next_section_no)+currect_section[-2:]
	print(next_section_no)

	if currect_section[0]=='1':
		max_credit = 28;

		first = set()
		second = set()
		load_1stcourses = CourseList.objects.filter(semester=1)
		for course in load_1stcourses:
			already_insert_check = TakenCourse.objects.filter(student_id__user=user, 
								course_code=course, semester=prev_sem)
			if already_insert_check:
				pass
			else:
				first.add(course)

		load_2ndcourses = CourseList.objects.filter(semester=2)
		for course in load_2ndcourses:
			already_insert_check = TakenCourse.objects.filter(student_id__user=user, 
								course_code=course, semester=new_semester)
			if already_insert_check:
				pass
			else:
				second.add(course)

		extra_course_to_be_load = {}

		for sem in range(3,9):
			load_courses = CourseList.objects.filter(semester=sem)
			for course in load_courses:

				already_insert_check = ApplyingCourse.objects.filter(student_id__user=user, 
								course_code=course, semester=new_semester)

				if already_insert_check:
					pass
				else:
					check_prerequisite = course.prerequisite
					if not (check_prerequisite):
						extra_course_to_be_load [course.course_code] = [course.course_code,course.course_title,course.credit_hour,course.semester]

		context = {'courses':first, 'courses2nd':second ,'extra_course_to_be_load':extra_course_to_be_load,
				'section':currect_section,'section2':next_section,'static':True}


	else:
		# calculating maximum crdit from previous semester taken courses
		max_credit = max_credit_calculate(user,prev_prev_sem)
		current_sem = int(currect_section[0])
		regular_course_to_be_load = {}
		extra_course_to_be_load = {}
		count = 0
		credit = 0

		for sem in range(1,9):
			load_courses = CourseList.objects.filter(semester=sem)
			for course in load_courses:
				taken_check = TakenCourse.objects.filter(student_id__user=user, 
								course_code=course, gpa__gte = 2.00)
				already_insert_check = TakenCourse.objects.filter(student_id__user=user, 
								course_code=course, semester=new_semester)
				already_insert_check_retaken = ApplyingCourse.objects.filter(student_id__user=user, 
								course_code=course, semester=new_semester)
				# print(taken_check)
				current_check = TakenCourse.objects.filter(student_id__user=user, 
								course_code=course).order_by('section')
				flag = False
				for chk in current_check:
					if chk.section == currect_section:
						flag = True
						break

				if taken_check or already_insert_check or already_insert_check_retaken or flag:
					pass
				else:
					check_prerequisite = course.prerequisite
					if check_prerequisite:
						taken_check = TakenCourse.objects.filter(student_id__user=user, 
										course_code__course_code=check_prerequisite, gpa__gte = 2.00)
						current_check = TakenCourse.objects.filter(student_id__user=user, 
								course_code__course_code=check_prerequisite).order_by('section')
						flag = False
						for chk in current_check:
							if chk.section == currect_section:
								flag = True
								break

						if taken_check or flag:
							count += 1
							credit += course.credit_hour
							if next_section_no == sem:
								regular_course_to_be_load [course.course_code] = [course.course_code,course.course_title,course.credit_hour,course.semester]
							else:
								extra_course_to_be_load [course.course_code] = [course.course_code,course.course_title,course.credit_hour,course.semester]
							print(course.course_code, course.semester, course.prerequisite)
					else:
						count += 1;
						credit += course.credit_hour
						if next_section_no == sem:
							regular_course_to_be_load [course.course_code] = [course.course_code,course.course_title,course.credit_hour,course.semester]
						else:
							extra_course_to_be_load [course.course_code] = [course.course_code,course.course_title,course.credit_hour,course.semester]
						print(course.course_code, course.semester, course.prerequisite)
						

		print(max_credit, credit)


		context = {'regular_course_to_be_load':regular_course_to_be_load,'extra_course_to_be_load':extra_course_to_be_load, 'static':False}

	return render(request,'student/pre-registration.html',context)


def max_credit_calculate(user,sem):
	gpa = gpa_calculate(user,sem)
	if gpa >= 3.75 and gpa <= 4.00:
		return 28
	elif gpa >= 3.50 and gpa <= 3.74:
		return 26
	elif gpa >= 2.75 and gpa <= 3.49:
		return 24
	elif gpa >= 2.25 and gpa <= 2.74:
		return 22
	elif gpa >= 2.00 and gpa <= 2.24:
		return 20
	elif gpa >= 1.70 and gpa <= 1.99:
		return 15
	else:
		return 12


def gpa_calculate(user,sem):
	taken_courses = TakenCourse.objects.filter(student_id__user=user,semester= sem)

	user = str(user)
	print(user)

	total_credit = 0
	total_credit_hour = 0

	for course in taken_courses:
		student = str(course.student_id)
		print(student)
		if student==user:
			print(course.semester, course.course_code,course.gpa)
			if course.gpa != None:
				total_credit += course.course_code.credit_hour * course.gpa
				total_credit_hour += course.course_code.credit_hour

	print('total_credit_hour', total_credit_hour)
	print('total_credit',total_credit)
	if total_credit == 0:
		return 1
	prev_sem_gpa = total_credit/total_credit_hour

	print(prev_sem_gpa)

	return prev_sem_gpa

def section_insert(student_obj, course_obj, semester, section):
	if section == '1AM':
		insert = Section1AM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '1BM':
		insert = Section1BM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '1CM':
		insert = Section1CM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '1DM':
		insert = Section1DM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '2AM':
		insert = Section2AM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '2BM':
		insert = Section2BM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '2CM':
		insert = Section2CM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '2DM':
		insert = Section2DM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '3AM':
		insert = Section3AM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '3BM':
		insert = Section3BM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '3CM':
		insert = Section3CM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '3DM':
		insert = Section3DM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '4AM':
		insert = Section4AM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '4BM':
		insert = Section4BM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '4CM':
		insert = Section4CM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)
	elif section == '4DM':
		insert = Section4DM.objects.get_or_create(student_id=student_obj,
				course_id = course_obj, status='REGULAR',semester=semester)





@login_required
def taken_courses(request):
	user = request.user
	student_obj = StudentProfile.objects.get(user=user)
	current_semester = SemesterSelection.objects.all()[0]
	new_semester = current_semester.semester
	if student_obj.section[0] == '1':
		taken = TakenCourse.objects.filter(student_id=student_obj)
		return render(request, 'student/taken-course.html',{'taken_courses':taken})
	else:
		taken = TakenCourse.objects.filter(student_id=student_obj, semester=new_semester)
		retaken = ApplyingCourse.objects.filter(student_id=student_obj, semester=new_semester)
		return render(request, 'student/taken-course.html',{'taken_courses':taken,'retaken_courses':retaken})

	

