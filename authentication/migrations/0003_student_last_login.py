# Generated by Django 4.2.4 on 2023-09-04 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_student_is_active_remove_student_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
