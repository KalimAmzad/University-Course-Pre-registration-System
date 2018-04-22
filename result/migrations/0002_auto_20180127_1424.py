# Generated by Django 2.0 on 2018-01-27 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20180127_1228'),
        ('account', '0008_remove_studentprofile_date_of_birth'),
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Result3rd',
            new_name='Result1',
        ),
        migrations.RenameModel(
            old_name='Result8th',
            new_name='Result2',
        ),
        migrations.RenameModel(
            old_name='Result5th',
            new_name='Result3',
        ),
        migrations.RenameModel(
            old_name='Result7th',
            new_name='Result4',
        ),
        migrations.RenameModel(
            old_name='Result4th',
            new_name='Result5',
        ),
        migrations.RenameModel(
            old_name='Result1st',
            new_name='Result6',
        ),
        migrations.RenameModel(
            old_name='Result2nd',
            new_name='Result7',
        ),
        migrations.RenameModel(
            old_name='Result6th',
            new_name='Result8',
        ),
        migrations.AlterModelOptions(
            name='result1',
            options={'verbose_name_plural': '1st Sem Result'},
        ),
        migrations.AlterModelOptions(
            name='result2',
            options={'verbose_name_plural': '2nd Sem Result'},
        ),
        migrations.AlterModelOptions(
            name='result3',
            options={'verbose_name_plural': '3rd Sem Result'},
        ),
        migrations.AlterModelOptions(
            name='result4',
            options={'verbose_name_plural': '4th Sem Result'},
        ),
        migrations.AlterModelOptions(
            name='result5',
            options={'verbose_name_plural': '5th Sem Result'},
        ),
        migrations.AlterModelOptions(
            name='result6',
            options={'verbose_name_plural': '6th Sem Result'},
        ),
        migrations.AlterModelOptions(
            name='result7',
            options={'verbose_name_plural': '7th Sem Result'},
        ),
        migrations.AlterModelOptions(
            name='result8',
            options={'verbose_name_plural': '8th Sem Result'},
        ),
    ]
