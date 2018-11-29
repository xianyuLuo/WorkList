from django.db import models
from datetime import date
from django.contrib.auth.models import User


class user(User):
    phone_number = models.CharField(max_length = 20, verbose_name = '联系电话', help_text = '用于接收通知')

    class Meta:
        verbose_name = "User"
        verbose_name_plural = verbose_name

class level(models.Model):
    level_name = models.CharField(max_length = 50, verbose_name = '事件等级', help_text= '事情等级，例：重要紧急')
    level_comment = models.TextField(max_length = 500, verbose_name = '备注', blank = True, help_text = '备注')

    def __str__(self):
        return self.level_name

    class Meta:
        verbose_name = "Level"
        verbose_name_plural = verbose_name

class job(models.Model):
    job_level = models.ForeignKey(level, on_delete = models.CASCADE, verbose_name = 'Job等级', help_text = '事件等级')
    job_user = models.ForeignKey(user, on_delete = models.CASCADE, verbose_name = 'Job归属', help_text = '任务归属')
    job_date = models.DateField(default = date.today(), verbose_name = '时间')
    job_isover = models.BooleanField(verbose_name = '是否完成', default = False)
    job_content = models.TextField(max_length = 500, verbose_name = 'Job', help_text = '详细信息')
    job_comment = models.TextField(max_length = 500, verbose_name = '备注', blank = True, help_text = '备注')

    def __str__(self):
        return self.job_content

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = verbose_name