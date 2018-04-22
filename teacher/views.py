from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from course.models import *
from section.models import *
from account.models import StudentProfile, TeacherProfile

@user_passes_test(lambda u: u.is_superuser)
def applying_courses(request):


	if request.method == 'POST':

		given = request.POST.getlist("course")
		sections = request.POST.getlist("section")
		sections = list(filter(None, sections))

		print(given,sections)

		dictionary = dict(zip(sections,given))

		for keys,values in dictionary.items():
			print(keys,values[:-7],values[-7:])
			student_id = str(values[-7:])
			course_id = values[:-8]
			print(student_id,course_id)
			semester = SemesterSelection.objects.all()[0]
			course_obj = CourseList.objects.get(course_code=course_id)
			student_obj = StudentProfile.objects.get(user__username=student_id)

			insert_course = TakenCourse.objects.get_or_create(student_id=student_obj,
				course_code = course_obj, status='IRREGULAR',semester=semester, section=keys)
			if keys == '1AM':
				insert_into_section = Section1AM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '1BM':
				insert_into_section = Section1BM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '1CM':
				insert_into_section = Section1CM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '1DM':
				insert_into_section = Section1DM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '2AM':
				insert_into_section = Section2AM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '2BM':
				insert_into_section = Section2BM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '2CM':
				insert_into_section = Section2CM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '2DM':
				insert_into_section = Section2DM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '3AM':
				insert_into_section = Section3AM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '3BM':
				insert_into_section = Section3BM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '3CM':
				insert_into_section = Section3CM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '3DM':
				insert_into_section = Section3DM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '4AM':
				insert_into_section = Section4AM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '4BM':
				insert_into_section = Section4BM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '4CM':
				insert_into_section = Section4CM.objects.get_or_create(student_id=student_obj, course_id=course_obj)
			elif keys == '4DM':
				insert_into_section = Section4DM.objects.get_or_create(student_id=student_obj, course_id=course_obj)

			delete_course = ApplyingCourse.objects.filter(student_id=student_obj,
				course_code = course_obj).delete()
	semester = SemesterSelection.objects.all()
	print(semester)

	courses = ApplyingCourse.objects.all()

	return render(request, 'teacher/applying_courses.html',{'applying_courses':courses})


@user_passes_test(lambda u: u.is_superuser)
def teacher_assign(request):

	if request.method == 'POST':

		teachers = request.POST.getlist("teacher")
		teachers = list(filter(None, teachers))
		courses = request.POST.getlist("course")
		courses = list(filter(None, courses))
		sections = request.POST.getlist("section")
		sections = list(filter(None, sections))

		total = min(len(teachers),len(courses),len(sections))

		for i in range(total):
			print(teachers[i], courses[i], sections[i])

			course_obj = CourseList.objects.get(course_code=courses[i])
			teacher_obj = TeacherProfile.objects.get(user__username=teachers[i])

			insert_course = TakenCourse.objects.filter(course_code = course_obj)
			for teacher in insert_course:
				teacher.teacher_id = teacher_obj
				teacher.save()

			if sections[i] == '1AM':
				insert_into_section = Section1AM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '1BM':
				insert_into_section = Section1BM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '1CM':
				insert_into_section = Section1CM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '1DM':
				insert_into_section = Section1DM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '2AM':
				insert_into_section = Section2AM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '2BM':
				insert_into_section = Section2BM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '2CM':
				insert_into_section = Section2CM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '2DM':
				insert_into_section = Section2DM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '3AM':
				insert_into_section = Section3AM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '3BM':
				insert_into_section = Section3BM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '3CM':
				insert_into_section = Section3CM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '3DM':
				insert_into_section = Section3DM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '4AM':
				insert_into_section = Section4AM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '4BM':
				insert_into_section = Section4BM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '4CM':
				insert_into_section = Section4CM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()
			elif sections[i] == '4DM':
				insert_into_section = Section4DM.objects.filter(course_id=course_obj)
				for teacher in insert_into_section:
					teacher.teacher_id = teacher_obj
					teacher.save()


	iteration = range(1,11)
	return render(request, 'teacher/teacher_assign.html', {'iteration': iteration})	