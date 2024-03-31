# Generated by Django 4.2.4 on 2023-09-04 19:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('publish_year', models.PositiveIntegerField()),
                ('barrow_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('returned', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=100)),
                ('return_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]