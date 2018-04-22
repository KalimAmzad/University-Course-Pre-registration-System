from django.db import models

from account.models import StudentProfile, TeacherProfile
from course.models import CourseList


class Result1(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList, blank=True, null=True,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5,decimal_places=3)

	def __str__(self):
		return str(self.student_id)

	class Meta:
		verbose_name_plural = '1st Sem Result'

class Result2(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList, blank=True, null=True,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5,decimal_places=3)

	def __str__(self):
		return str(self.student_id)

	class Meta:
		verbose_name_plural = '2nd Sem Result'

class Result3(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList, blank=True, null=True,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5,decimal_places=3)

	def __str__(self):
		return str(self.student_id)

	class Meta:
		verbose_name_plural = '3rd Sem Result'

class Result4(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList, blank=True, null=True,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5,decimal_places=3)

	def __str__(self):
		return str(self.student_id)

	class Meta:
		verbose_name_plural = '4th Sem Result'

class Result5(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList, blank=True, null=True,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5,decimal_places=3)

	def __str__(self):
		return str(self.student_id)

	class Meta:
		verbose_name_plural = '5th Sem Result'

class Result6(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList, blank=True, null=True,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5,decimal_places=3)

	def __str__(self):
		return str(self.student_id)

	class Meta:
		verbose_name_plural = '6th Sem Result'

class Result7(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList, blank=True, null=True,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5,decimal_places=3)

	def __str__(self):
		return str(self.student_id)

	class Meta:
		verbose_name_plural = '7th Sem Result'

class Result8(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList, blank=True, null=True,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5,decimal_places=3)

	def __str__(self):
		return str(self.student_id)

	class Meta:
		verbose_name_plural = '8th Sem Result'
