# Generated by Django 2.1.2 on 2018-10-31 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_auto_20181031_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='level_comment',
            field=models.TextField(blank=True, help_text='备注', max_length=500, verbose_name='备注'),
        ),
    ]
