# Generated by Django 2.0 on 2018-01-26 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0008_remove_studentprofile_date_of_birth'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result1st',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.DecimalField(decimal_places=3, max_digits=5)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Result2nd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.DecimalField(decimal_places=3, max_digits=5)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Result3rd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.DecimalField(decimal_places=3, max_digits=5)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Result4th',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.DecimalField(decimal_places=3, max_digits=5)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Result5th',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.DecimalField(decimal_places=3, max_digits=5)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Result6th',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.DecimalField(decimal_places=3, max_digits=5)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Result7th',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.DecimalField(decimal_places=3, max_digits=5)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Result8th',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.DecimalField(decimal_places=3, max_digits=5)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
            ],
        ),
    ]
