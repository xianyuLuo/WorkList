from .models import level, job, user
from django.contrib import admin, messages

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'first_name', 'last_name', 'is_staff']
    list_per_page = 20

class LevelAdmin(admin.ModelAdmin):
    list_display = ['level_name', 'level_comment']
    list_filter = ['level_name']
    search_fields = ['level_name']
    list_per_page = 10

class JobAdmin(admin.ModelAdmin):
    list_display = ['job_level', 'job_user', 'job_content', 'job_date', 'job_isover', 'job_comment']
    list_filter = ['job_level', 'job_date', 'job_user', 'job_content', 'job_isover']
    search_fields = ['job_level', 'job_date', 'job_user']
    list_per_page = 30
    actions = ['is_over', 'is_nover']

    def is_over(self, request, queryset):
        row = queryset.update(job_isover = True)
        msg = "{} 个job被标记为已完成".format(row)
        self.message_user(request, msg, messages.SUCCESS)

    def is_nover(self, request, queryset):
        row = queryset.update(job_isover = False)
        msg = "{}个job被标记为未完成".format(row)
        self.message_user(request, msg, messages.SUCCESS)

    is_over.short_description = "标记为已完成"
    is_nover.short_description = "标记为未完成"

admin.site.register(user, UserAdmin)
admin.site.register(level, LevelAdmin)
admin.site.register(job, JobAdmin)