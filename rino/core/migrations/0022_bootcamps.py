# Generated by Django 5.1.3 on 2024-12-01 19:09

import core.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_teammembers_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootcamps',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('price_per_month', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='قیمت هر ماه')),
                ('feature_1', models.CharField(max_length=50, verbose_name='فیچر 1')),
                ('feature_2', models.CharField(max_length=50, verbose_name='فیچر 2')),
                ('feature_3', models.CharField(max_length=50, verbose_name='فیچر 3')),
                ('feature_4', models.CharField(max_length=50, verbose_name='فیچر 4')),
                ('image', models.ImageField(upload_to=core.models.Bootcamps.get_upload_path)),
            ],
            options={
                'verbose_name': 'بوت کمپ آموزشی',
                'verbose_name_plural': 'بوت کمپ های آموزشی',
            },
        ),
    ]