# Generated by Django 5.1.3 on 2024-11-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_counters'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='مثلا: توسعه', max_length=50, verbose_name='عنوان')),
                ('progress_precentage', models.PositiveIntegerField(help_text='مثلا یک عدد بین 0 تا 100', verbose_name='درصد پیشرفت')),
                ('color', models.CharField(default='#3374ff', help_text='رنگ زرد : #f0ff33', max_length=50, verbose_name='رنگ پیشرفت')),
            ],
            options={
                'verbose_name': 'مهارت',
                'verbose_name_plural': 'مهارت ها',
            },
        ),
        migrations.CreateModel(
            name='SkillSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیح')),
                ('image', models.ImageField(upload_to='skill-section/', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'بخش مهارت',
                'verbose_name_plural': 'بخش مهارت ها',
            },
        ),
    ]