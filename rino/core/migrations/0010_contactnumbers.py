# Generated by Django 5.1.3 on 2024-11-27 19:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_skillsection_updated_at_skillsection_upload_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='عدد باید با فرمت صحیح و با 09 شروع شود', regex='^09\\d{9}$')], verbose_name='شماره تماس')),
                ('is_staff', models.BooleanField(default=True, verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'شماره تماس شرکت',
                'verbose_name_plural': 'شماره تماس های شرکت',
            },
        ),
    ]