# Generated by Django 5.1.3 on 2024-11-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_serviceintroductions_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('video_url', models.URLField(verbose_name='لینک ویدیو')),
            ],
            options={
                'verbose_name_plural': 'Call Area',
            },
        ),
    ]