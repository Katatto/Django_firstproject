# Generated by Django 4.2.5 on 2023-09-16 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudprojectapp', '0003_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=10),
        ),
    ]
