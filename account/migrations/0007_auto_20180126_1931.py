# Generated by Django 2.0 on 2018-01-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20180126_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='section',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='semester',
            field=models.CharField(max_length=32),
        ),
    ]
