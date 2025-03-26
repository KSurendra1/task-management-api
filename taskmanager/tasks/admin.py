from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'task_type', 'status', 'created_at', 'get_assigned_users')
    list_filter = ('task_type', 'status', 'created_at')
    search_fields = ('name', 'description')
    filter_horizontal = ('assigned_users',)
    
    def get_assigned_users(self, obj):
        return ", ".join([user.username for user in obj.assigned_users.all()])
    get_assigned_users.short_description = 'Assigned Users'

admin.site.register(Task, TaskAdmin)

