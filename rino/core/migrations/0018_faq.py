# Generated by Django 5.1.3 on 2024-11-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_callarea_created_at_callarea_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='سوال')),
                ('answer', models.TextField(verbose_name='پاسخ')),
                ('number', models.PositiveIntegerField(verbose_name='شماره سوال')),
                ('icon', models.CharField(default='fa-sharp fa-solid fa-circle-check', max_length=50, verbose_name='آیکون')),
            ],
            options={
                'verbose_name': 'سوال متداول',
                'verbose_name_plural': 'سوالات متداول',
                'ordering': ['number'],
            },
        ),
    ]