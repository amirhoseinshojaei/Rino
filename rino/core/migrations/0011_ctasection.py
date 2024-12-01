# Generated by Django 5.1.3 on 2024-11-28 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_contactnumbers'),
    ]

    operations = [
        migrations.CreateModel(
            name='CtaSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('video_url', models.URLField(verbose_name='لینک ویدیو')),
                ('button_text', models.CharField(help_text='مثلا ویدیو های بیشتر', max_length=50, verbose_name='متن دکمه')),
                ('button_url', models.URLField(verbose_name='لینک دکمه')),
                ('bg_image', models.ImageField(upload_to='cta_section/background_image/', verbose_name='تصویر بک گراند')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
            ],
            options={
                'verbose_name': 'cta-section',
                'verbose_name_plural': 'cta-section',
            },
        ),
    ]
