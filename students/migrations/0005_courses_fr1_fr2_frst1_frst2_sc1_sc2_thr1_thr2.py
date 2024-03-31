# Generated by Django 4.2.4 on 2023-09-03 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_rename_general_book_generalbook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=255)),
                ('image_path', models.CharField(max_length=255)),
                ('book_author', models.CharField(max_length=100)),
                ('publish_year', models.IntegerField(blank=True, null=True)),
                ('file_path', models.CharField(max_length=255)),
                ('branch', models.CharField(blank=True, max_length=50, null=True)),
                ('genre', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fr1',
            fields=[
                ('courses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.courses')),
            ],
            bases=('students.courses',),
        ),
        migrations.CreateModel(
            name='fr2',
            fields=[
                ('courses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.courses')),
            ],
            bases=('students.courses',),
        ),
        migrations.CreateModel(
            name='frst1',
            fields=[
                ('courses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.courses')),
            ],
            bases=('students.courses',),
        ),
        migrations.CreateModel(
            name='frst2',
            fields=[
                ('courses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.courses')),
            ],
            bases=('students.courses',),
        ),
        migrations.CreateModel(
            name='sc1',
            fields=[
                ('courses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.courses')),
            ],
            bases=('students.courses',),
        ),
        migrations.CreateModel(
            name='sc2',
            fields=[
                ('courses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.courses')),
            ],
            bases=('students.courses',),
        ),
        migrations.CreateModel(
            name='thr1',
            fields=[
                ('courses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.courses')),
            ],
            bases=('students.courses',),
        ),
        migrations.CreateModel(
            name='thr2',
            fields=[
                ('courses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.courses')),
            ],
            bases=('students.courses',),
        ),
    ]
