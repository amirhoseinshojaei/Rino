# Generated by Django 5.1.3 on 2024-11-29 13:33

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammembers',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.TeamMembers.get_upload_path),
        ),
    ]