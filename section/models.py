from django.db import models

from account.models import StudentProfile, TeacherProfile
from course.models import CourseList

class Section1AM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)

	class Meta:
		verbose_name_plural = '1AM'



class Section1BM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '1BM'	


class Section1CM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '1CM'

class Section1DM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '1DM'

class Section2AM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '2AM'

class Section2BM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '2BM'

class Section2CM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '2CM'

class Section2DM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '2DM'

class Section3AM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '3AM'

class Section3BM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '3BM'

class Section3CM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '3CM'

class Section3DM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '3DM'

class Section4AM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '4AM'

class Section4BM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '4BM'

class Section4CM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '4CM'

class Section4DM(models.Model):
	student_id = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,)
	course_id = models.ForeignKey(CourseList,
        on_delete=models.CASCADE,)
	teacher_id = models.ForeignKey(TeacherProfile,
        on_delete=models.CASCADE,blank=True,null=True)
	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)
	status_choices = (
    ('REGULAR', 'Regular'),
    ('IRREGULAR', 'Irregular'),
)
	status = models.CharField(max_length=10,choices=status_choices,default='REGULAR')
	semester = models.CharField(max_length=32,null=True,blank=True)
	class Meta:
			verbose_name_plural = '4DM'

# class Section2AM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section2BM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section2CM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section2DM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section3AM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section3BM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section3CM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section3DM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section4AM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section4BM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section4CM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section4DM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section5AM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section5BM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section5CM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section5DM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section6AM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section6BM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section6CM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section6DM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section7AM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section7BM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section7CM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section7DM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section8AM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section8BM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section8CM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id

# class Section8DM(models.Model):
# 	student_id = models.ForeignKey(StudentProfile)
# 	course_id = models.ForeignKey(CourseList)
# 	teacher_id = models.ForeignKey(TeacherProfile)
# 	result = models.DecimalField(max_digits=5, decimal_places=3, blank=True,null=True)

# 	def __str__(self):
# 		return self.student_id
