from django.db import models

from account.models import StudentProfile, TeacherProfile
from course.models import CourseList

class TeacherAssign(models.Model):
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	section = models.CharField(max_length=5)

	def __str__(self):
		return self.teacher_id