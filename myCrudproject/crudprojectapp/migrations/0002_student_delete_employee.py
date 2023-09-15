# Generated by Django 4.2.5 on 2023-09-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'tblstudent',
            },
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
