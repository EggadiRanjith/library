# Generated by Django 4.2.4 on 2023-09-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_student_id_alter_student_roll_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
