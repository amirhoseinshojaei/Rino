# Generated by Django 5.1.3 on 2024-11-28 17:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_callarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='callarea',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='callarea',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]