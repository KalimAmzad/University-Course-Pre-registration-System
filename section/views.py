from django.shortcuts import render,redirect
from django.http import Http404, HttpResponseNotFound 
from django.contrib.auth.decorators import user_passes_test


from account.models import StudentProfile,TeacherProfile
from course.models import *
from .models import *


@user_passes_test(lambda u: u.is_superuser)
def check_section(request):

	if request.method =="POST":

		course = request.POST.get("course")
		section = request.POST.get("semester")
		

		sem = SemesterSelection.objects.all()[0]
		seme = sem.semester
		if(seme[0:3]=='AUT' or seme[0:3]=='aut' or seme[0:3]=='Aut'):
			sem = 'SP'
			prev_sem = sem + ' - ' + str(int(seme[-2:]))
		else:
			sem = 'AUT'
			prev_sem = sem + ' - ' + str(int(seme[-2:])-1)
		print(course,section,prev_sem)
		if course != '' and section != '':
			course_obj = CourseList.objects.get(course_code=course)
			if section == '1':
				sec1 = Section1AM.objects.filter(course_id=course_obj,semester=prev_sem)
				sec2 = Section1BM.objects.filter(course_id=course_obj,semester=prev_sem)
				sec3 = Section1CM.objects.filter(course_id=course_obj,semester=prev_sem)
				sec4 = Section1DM.objects.filter(course_id=course_obj,semester=prev_sem)
			elif section == '2':
				sec1 = Section2AM.objects.filter(course_id=course_obj,semester=seme)
				sec2 = Section2BM.objects.filter(course_id=course_obj,semester=seme)
				sec3 = Section2CM.objects.filter(course_id=course_obj,semester=seme)
				sec4 = Section2DM.objects.filter(course_id=course_obj,semester=seme)
			elif section == '3':
				sec1 = Section3AM.objects.filter(course_id=course_obj,semester=seme)
				sec2 = Section3BM.objects.filter(course_id=course_obj,semester=seme)
				sec3 = Section3CM.objects.filter(course_id=course_obj,semester=seme)
				sec4 = Section3DM.objects.filter(course_id=course_obj,semester=seme)
			elif section == '4':
				sec1 = Section4AM.objects.filter(course_id=course_obj,semester=seme)
				sec2 = Section4BM.objects.filter(course_id=course_obj,semester=seme)
				sec3 = Section4CM.objects.filter(course_id=course_obj,semester=seme)
				sec4 = Section4DM.objects.filter(course_id=course_obj,semester=seme)
			elif section == '5':
				sec1 = Section5AM.objects.filter(course_id=course_obj,semester=seme)
				sec2 = Section5BM.objects.filter(course_id=course_obj,semester=seme)
				sec3 = Section5CM.objects.filter(course_id=course_obj,semester=seme)
				sec4 = Section5DM.objects.filter(course_id=course_obj,semester=seme)
			elif section == '6':
				sec1 = Section6AM.objects.filter(course_id=course_obj,semester=seme)
				sec2 = Section6BM.objects.filter(course_id=course_obj,semester=seme)
				sec3 = Section6CM.objects.filter(course_id=course_obj,semester=seme)
				sec4 = Section6DM.objects.filter(course_id=course_obj,semester=seme)
			elif section == '7':
				sec1 = Section7AM.objects.filter(course_id=course_obj,semester=seme)
				sec2 = Section7BM.objects.filter(course_id=course_obj,semester=seme)
				sec3 = Section7CM.objects.filter(course_id=course_obj,semester=seme)
				sec4 = Section7DM.objects.filter(course_id=course_obj,semester=seme)
			elif section == '8':
				sec1 = Section8AM.objects.filter(course_id=course_obj,semester=seme)
				sec2 = Section8BM.objects.filter(course_id=course_obj,semester=seme)
				sec3 = Section8CM.objects.filter(course_id=course_obj,semester=seme)
				sec4 = Section8DM.objects.filter(course_id=course_obj,semester=seme)
		elif section != '':
			if section == '1':
				sec1 = Section1AM.objects.filter(semester=prev_sem)
				sec2 = Section1BM.objects.filter(semester=prev_sem)
				sec3 = Section1CM.objects.filter(semester=prev_sem)
				sec4 = Section1DM.objects.filter(semester=prev_sem)
			elif section == '2':
				sec1 = Section2AM.objects.filter(semester=seme)
				sec2 = Section2BM.objects.filter(semester=seme)
				sec3 = Section2CM.objects.filter(semester=seme)
				sec4 = Section2DM.objects.filter(semester=seme)
			elif section == '3':
				sec1 = Section3AM.objects.filter(semester=seme)
				sec2 = Section3BM.objects.filter(semester=seme)
				sec3 = Section3CM.objects.filter(semester=seme)
				sec4 = Section3DM.objects.filter(semester=seme)
			elif section == '4':
				sec1 = Section4AM.objects.filter(semester=seme)
				sec2 = Section4BM.objects.filter(semester=seme)
				sec3 = Section4CM.objects.filter(semester=seme)
				sec4 = Section4DM.objects.filter(semester=seme)
			elif section == '5':
				sec1 = Section5AM.objects.filter(semester=seme)
				sec2 = Section5BM.objects.filter(semester=seme)
				sec3 = Section5CM.objects.filter(semester=seme)
				sec4 = Section5DM.objects.filter(semester=seme)
			elif section == '6':
				sec1 = Section6AM.objects.filter(semester=seme)
				sec2 = Section6BM.objects.filter(semester=seme)
				sec3 = Section6CM.objects.filter(semester=seme)
				sec4 = Section6DM.objects.filter(semester=seme)
			elif section == '7':
				sec1 = Section7AM.objects.filter(semester=seme)
				sec2 = Section7BM.objects.filter(semester=seme)
				sec3 = Section7CM.objects.filter(semester=seme)
				sec4 = Section7DM.objects.filter(semester=seme)
			elif section == '8':
				sec1 = Section8AM.objects.filter(semester=seme)
				sec2 = Section8BM.objects.filter(semester=seme)
				sec3 = Section8CM.objects.filter(semester=seme)
				sec4 = Section8DM.objects.filter(semester=seme)
		a = set([])
		b = set([])
		c = set([])
		d = set([])
		for i in sec1:
			a.add(i.student_id)
		for i in sec2:
			b.add(i.student_id)
		for i in sec3:
			c.add(i.student_id)
		for i in sec4:
			d.add(i.student_id)


		total = len(a) + len(b) + len(c) + len(d)

		return render(request, 'section/check_section.html', {"sec1":a, "total_sec1":len(a), "sec2":b,
			"total_sec2":len(b), "sec3":c,"total_sec3":len(c),"sec4":d,"total_sec4":len(d),
			"total":total, "section":section, "course":course})

	return render(request, 'section/check_section_form.html',{})



@user_passes_test(lambda u: u.is_superuser)
def merge_section(request):

	if request.method == "POST":
		per_section = request.POST.get("per_section")
		section = request.POST.get("section")

		sem = SemesterSelection.objects.all()[0]
		seme = sem.semester
		print(per_section,section,seme)

		if per_section !='' and section != '':
			if section == '1':

				sec1 = Section1AM.objects.filter(semester=seme).order_by('student_id')
				unique1 = set()
				for i in sec1:
					unique1.add(i.student_id)
				print(len(unique1))

				sec2 = Section1BM.objects.filter(semester=seme).order_by('student_id')
				unique2 = set()
				for i in sec2:
					unique2.add(i.student_id)
				print(len(unique2))

				sec3 = Section1CM.objects.filter(semester=seme).order_by('student_id')
				unique3 = set()
				for i in sec3:
					unique3.add(i.student_id)
				print(len(unique3))

				sec4 = Section1DM.objects.filter(semester=seme).order_by('student_id')
				unique4 = set()
				for i in sec4:
					unique4.add(i.student_id)
				print(len(unique4))

				if len(unique1) < int(per_section):
					req = int(per_section) - len(unique1)
					print(req)
					if req < len(unique2):
						insert = list(unique2)[:req]
						print(insert)
						for i in insert:
							new_sec2 = Section1BM.objects.filter(student_id=i,semester=seme)
							for j in new_sec2:
								ins = Section1AM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()
							new_sec2.delete()
							unique2.discard(i)
					else:
						insert = list(unique2)
						for i in insert:
							new_sec2 = Section1BM.objects.filter(student_id=i,semester=seme)
							for j in new_sec2:
								ins = Section1AM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()
							new_sec2.delete()
							unique2.discard(i)


				if len(unique2) < int(per_section):
					req = int(per_section) - len(unique2)
					print(req)
					if req < len(unique3):
						insert = list(unique3)[:req]
						print(insert)
						for i in insert:
							new_sec3 = Section1CM.objects.filter(student_id=i,semester=seme)
							for j in new_sec3:
								ins = Section1BM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()
							new_sec3.delete()
							unique3.discard(i)
					else:
						insert = list(unique3)
						for i in insert:
							new_sec3 = Section1CM.objects.filter(student_id=i,semester=seme)
							for j in new_sec3:
								ins = Section1BM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()
							new_sec3.delete()
							unique3.discard(i)
					# print(unique3)


				if len(unique3) < int(per_section):
					req = int(per_section) - len(unique3)
					print(req)
					if req < len(unique4):
						insert = list(unique4)[:req]
						print(insert)
						for i in insert:
							new_sec4 = Section1DM.objects.filter(student_id=i,semester=seme)
							for j in new_sec4:
								ins = Section1CM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()
							new_sec4.delete()
							unique4.discard(i)
					else:
						insert = list(unique4)
						for i in insert:
							new_sec4 = Section1DM.objects.filter(student_id=i,semester=seme)
							for j in new_sec4:
								ins = Section1CM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()
							new_sec4.delete()
							unique4.discard(i)
					# print(unique4)
			elif section == '2':
				sec1 = Section2AM.objects.filter(semester=seme).order_by('student_id')
				unique1 = set()
				for i in sec1:
					unique1.add(i.student_id)
				print(len(unique1))

				sec2 = Section2BM.objects.filter(semester=seme).order_by('student_id')
				unique2 = set()
				for i in sec2:
					unique2.add(i.student_id)
				print(len(unique2))

				sec3 = Section2CM.objects.filter(semester=seme).order_by('student_id')
				unique3 = set()
				for i in sec3:
					unique3.add(i.student_id)
				print(len(unique3))

				sec4 = Section2DM.objects.filter(semester=seme).order_by('student_id')
				unique4 = set()
				for i in sec4:
					unique4.add(i.student_id)
				print(len(unique4))

				if len(unique1) < int(per_section):
					req = int(per_section) - len(unique1)
					print(req)
					if req < len(unique2):
						insert = list(unique2)[:req]
						print(insert)
						for i in insert:
							new_sec2 = Section2BM.objects.filter(student_id=i,semester=seme)
							for j in new_sec2:
								ins = Section2AM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '2AM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '2AM'
									taken_course.save()

							new_sec2.delete()
							unique2.discard(i)
					else:
						insert = list(unique2)
						for i in insert:
							new_sec2 = Section2BM.objects.filter(student_id=i,semester=seme)
							for j in new_sec2:
								ins = Section2AM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()
								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '2AM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '2AM'
									taken_course.save()

							new_sec2.delete()
							unique2.discard(i)


				if len(unique2) < int(per_section):
					req = int(per_section) - len(unique2)
					print(req)
					if req < len(unique3):
						insert = list(unique3)[:req]
						print(insert)
						for i in insert:
							new_sec3 = Section2CM.objects.filter(student_id=i,semester=seme)
							for j in new_sec3:
								ins = Section2BM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()
								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '2BM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '2BM'
									taken_course.save()
							new_sec3.delete()
							unique3.discard(i)
					else:
						insert = list(unique3)
						for i in insert:
							new_sec3 = Section2CM.objects.filter(student_id=i,semester=seme)
							for j in new_sec3:
								ins = Section2BM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()
								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '2BM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '2BM'
									taken_course.save()

							new_sec3.delete()
							unique3.discard(i)
					# print(unique3)


				if len(unique3) < int(per_section):
					req = int(per_section) - len(unique3)
					print(req)
					if req < len(unique4):
						insert = list(unique4)[:req]
						print(insert)
						for i in insert:
							new_sec4 = Section2DM.objects.filter(student_id=i,semester=seme)
							for j in new_sec4:
								ins = Section2CM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()
								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '2CM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '2CM'
									taken_course.save()

							new_sec4.delete()
							unique4.discard(i)
					else:
						insert = list(unique4)
						for i in insert:
							new_sec4 = Section2DM.objects.filter(student_id=i,semester=seme)
							for j in new_sec4:
								ins = Section2CM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()
								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '2CM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '2CM'
									taken_course.save()

							new_sec4.delete()
							unique4.discard(i)
					# print(unique4)

			elif section == '3':
				sec1 = Section3AM.objects.filter(semester=seme).order_by('student_id')
				unique1 = set()

				for i in sec1:
					unique1.add(i.student_id)
				print(len(unique1))

				sec2 = Section3BM.objects.filter(semester=seme).order_by('student_id')
				unique2 = set()
				for i in sec2:
					unique2.add(i.student_id)
				print(len(unique2))

				sec3 = Section3CM.objects.filter(semester=seme).order_by('student_id')
				unique3 = set()
				for i in sec3:
					unique3.add(i.student_id)
				print(len(unique3))

				sec4 = Section3DM.objects.filter(semester=seme).order_by('student_id')
				unique4 = set()
				for i in sec4:
					unique4.add(i.student_id)
				print(len(unique4))

				if len(unique1) < int(per_section):
					req = int(per_section) - len(unique1)
					print(req)
					if req < len(unique2):
						insert = list(unique2)[:req]
						print(insert)
						for i in insert:
							new_sec2 = Section3BM.objects.filter(student_id=i,semester=seme)
							for j in new_sec2:
								ins = Section3AM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '3AM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '3AM'
									taken_course.save()

							new_sec2.delete()
							unique2.discard(i)
					else:
						insert = list(unique2)
						for i in insert:
							new_sec2 = Section3BM.objects.filter(student_id=i,semester=seme)
							for j in new_sec2:
								ins = Section3AM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '3AM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '3AM'
									taken_course.save()

							new_sec2.delete()
							unique2.discard(i)


				if len(unique2) < int(per_section):
					req = int(per_section) - len(unique2)
					print(req)
					if req < len(unique3):
						insert = list(unique3)[:req]
						print(insert)
						for i in insert:
							new_sec3 = Section3CM.objects.filter(student_id=i,semester=seme)
							for j in new_sec3:
								ins = Section3BM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '3BM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '3BM'
									taken_course.save()

							new_sec3.delete()
							unique3.discard(i)
					else:
						insert = list(unique3)
						for i in insert:
							new_sec3 = Section3CM.objects.filter(student_id=i,semester=seme)
							for j in new_sec3:
								ins = Section3BM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '3BM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '3BM'
									taken_course.save()

							new_sec3.delete()
							unique3.discard(i)
					# print(unique3)


				if len(unique3) < int(per_section):
					req = int(per_section) - len(unique3)
					print(req)
					if req < len(unique4):
						insert = list(unique4)[:req]
						print(insert)
						for i in insert:
							new_sec4 = Section3DM.objects.filter(student_id=i,semester=seme)
							for j in new_sec4:
								ins = Section3CM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '3CM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '3CM'
									taken_course.save()

							new_sec4.delete()
							unique4.discard(i)
					else:
						insert = list(unique4)
						for i in insert:
							new_sec4 = Section3DM.objects.filter(student_id=i,semester=seme)
							for j in new_sec4:
								ins = Section3CM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '3CM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '3CM'
									taken_course.save()

							new_sec4.delete()
							unique4.discard(i)
					# print(unique4)

			elif section == '4':
				sec1 = Section4AM.objects.filter(semester=seme).order_by('student_id')
				unique1 = ()
				for i in sec1:
					unique1.add(i.student_id)
				print(len(unique1))

				sec2 = Section4BM.objects.filter(semester=seme).order_by('student_id')
				unique2 = ()
				for i in sec2:
					unique2.add(i.student_id)
				print(len(unique2))

				sec3 = Section4CM.objects.filter(semester=seme).order_by('student_id')
				unique3 = ()
				for i in sec3:
					unique3.add(i.student_id)
				print(len(unique3))

				sec4 = Section4DM.objects.filter(semester=seme).order_by('student_id')
				unique4 = ()
				for i in sec4:
					unique4.add(i.student_id)
				print(len(unique4))

				if len(unique1) < int(per_section):
					req = int(per_section) - len(unique1)
					print(req)
					if req < len(unique2):
						insert = list(unique2)[:req]
						print(insert)
						for i in insert:
							new_sec2 = Section4BM.objects.filter(student_id=i,semester=seme)
							for j in new_sec2:
								ins = Section4AM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '4AM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '4AM'
									taken_course.save()

							new_sec2.delete()
							unique2.discard(i)
					else:
						insert = list(unique2)
						for i in insert:
							new_sec2 = Section4BM.objects.filter(student_id=i,semester=seme)
							for j in new_sec2:
								ins = Section4AM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '4AM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '4AM'
									taken_course.save()

							new_sec2.delete()
							unique2.discard(i)


				if len(unique2) < int(per_section):
					req = int(per_section) - len(unique2)
					print(req)
					if req < len(unique3):
						insert = list(unique3)[:req]
						print(insert)
						for i in insert:
							new_sec3 = Section4CM.objects.filter(student_id=i,semester=seme)
							for j in new_sec3:
								ins = Section4BM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '4BM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '4BM'
									taken_course.save()

							new_sec3.delete()
							unique3.discard(i)
					else:
						insert = list(unique3)
						for i in insert:
							new_sec3 = Section4CM.objects.filter(student_id=i,semester=seme)
							for j in new_sec3:
								ins = Section4BM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '4BM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '4BM'
									taken_course.save()

							new_sec3.delete()
							unique3.discard(i)
					# print(unique3)


				if len(unique3) < int(per_section):
					req = int(per_section) - len(unique3)
					print(req)
					if req < len(unique4):
						insert = list(unique4)[:req]
						print(insert)
						for i in insert:
							new_sec4 = Section4DM.objects.filter(student_id=i,semester=seme)
							for j in new_sec4:
								ins = Section4CM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '4CM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '4CM'
									taken_course.save()

							new_sec4.delete()
							unique4.discard(i)
					else:
						insert = list(unique4)
						for i in insert:
							new_sec4 = Section4DM.objects.filter(student_id=i,semester=seme)
							for j in new_sec4:
								ins = Section4CM.objects.create(student_id=j.student_id,course_id=j.course_id,
									semester=seme,teacher_id=j.teacher_id,status=j.status)
								ins.save()

								student_section_update = StudentProfile.objects.get(user__username=j.student_id)
								student_section_update.section = '4CM'
								student_section_update.save()

								taken_course_update = TakenCourse.objects.filter(student_id=j.student_id,semester=seme)
								for taken_course in taken_course_update:
									taken_course.section = '4CM'
									taken_course.save()

							new_sec4.delete()
							unique4.discard(i)
					# print(unique4)


					


	return render(request, 'section/merge_section.html',{})
