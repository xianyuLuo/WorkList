# Generated by Django 2.1.2 on 2018-10-31 08:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20181029_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_content',
            field=models.TextField(help_text='详细信息', max_length=500, verbose_name='Job'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_date',
            field=models.DateField(default=datetime.date(2018, 10, 31), verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_level',
            field=models.ForeignKey(help_text='事件等级', on_delete=django.db.models.deletion.CASCADE, to='job.level', verbose_name='Job等级'),
        ),
    ]
