# Generated by Django 4.2.4 on 2023-09-04 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_remove_fr1_courses_ptr_remove_fr2_courses_ptr_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='courses',
        ),
    ]