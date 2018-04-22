from django.db import models

from account.models import StudentProfile, TeacherProfile

class CourseList(models.Model):
	course_code = models.CharField(max_length=20)
	course_title = models.CharField(max_length=256)
	contact_hour = models.IntegerField()
	credit_hour = models.DecimalField(max_digits=5, decimal_places=2)
	prerequisite = models.CharField(max_length=10,blank=True, null= True)
	semester = models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.course_code

	class Meta:
		verbose_name_plural = 'All courses List'

class CompletedCouse1(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_code = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5, decimal_places=3)
	section = models.CharField(max_length=5)
	semester = models.CharField(max_length=32,null=True,blank=True)
	def __str__(self):
		return str(self.course_code)

	class Meta:
		verbose_name_plural = 'Completed 1st sem courses'

class CompletedCouse2(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_code = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5, decimal_places=3)
	semester = models.CharField(max_length=32,null=True,blank=True)
	section = models.CharField(max_length=5)

	def __str__(self):
		return str(self.course_code)

	class Meta:
		verbose_name_plural = 'Completed 2nd sem courses'

class CompletedCouse3(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_code = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5, decimal_places=3)
	semester = models.CharField(max_length=32,null=True,blank=True)
	section = models.CharField(max_length=5)

	def __str__(self):
		return str(self.course_code)

	class Meta:
		verbose_name_plural = 'Completed 3rd sem courses' 

class CompletedCouse4(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_code = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5, decimal_places=3)
	semester = models.CharField(max_length=32,null=True,blank=True)
	section = models.CharField(max_length=5)

	def __str__(self):
		return str(self.course_code)

	class Meta:
		verbose_name_plural = 'Completed 4th sem courses'

class CompletedCouse5(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_code = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5, decimal_places=3)
	semester = models.CharField(max_length=32,null=True,blank=True)
	section = models.CharField(max_length=5)

	def __str__(self):
		return str(self.course_code)

	class Meta:
		verbose_name_plural = 'Completed 5th sem courses'

class CompletedCouse6(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_code = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5, decimal_places=3)
	semester = models.CharField(max_length=32,null=True,blank=True)
	section = models.CharField(max_length=5)

	def __str__(self):
		return str(self.course_code)	

	class Meta:
		verbose_name_plural = 'Completed 6th sem courses'

class CompletedCouse7(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_code = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5, decimal_places=3)
	semester = models.CharField(max_length=32,null=True,blank=True)
	section = models.CharField(max_length=5)

	def __str__(self):
		return str(self.course_code)

	class Meta:
		verbose_name_plural = 'Completed 7th sem courses'

class CompletedCouse8(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_code = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,)
	gpa = models.DecimalField(max_digits=5, decimal_places=3)
	semester = models.CharField(max_length=32,null=True,blank=True)
	section = models.CharField(max_length=5)

	def __str__(self):
		return str(self.course_code)

	class Meta:
		verbose_name_plural = 'Completed 8th sem courses'


class ApplyingCourse(models.Model):
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)

	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,null=True,blank=True)
	course_code = models.ForeignKey(CourseList,
        on_delete=models.CASCADE)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	section = models.CharField(max_length=5,null=True,blank=True)

	def __str__(self):
		return str(self.course_code)

	class Meta:
		verbose_name_plural = 'Applying Courses'
		ordering = ['course_code__semester','course_code','student_id']



class TakenCourse(models.Model):
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')

	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,null=True,blank=True)
	course_code = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	semester = models.CharField(max_length=32,null=True,blank=True)
	section = models.CharField(max_length=5)
	gpa = models.DecimalField(max_digits=5,decimal_places=3,null=True,blank=True)

	def __str__(self):
		return str(self.course_code)

	class Meta:
		verbose_name_plural = 'Taken Courses'
		ordering = ['course_code__semester','course_code']

class SemesterSelection(models.Model):
	semester = models.CharField(max_length=32,unique=True)

	def __str__(self):
		return self.semester

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Semester Selection"