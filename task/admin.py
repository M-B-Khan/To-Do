from django.contrib import admin
from .models import Task

class AdminTask(admin.ModelAdmin):
    list_display = ('title','description', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_at', 'updated_at')
    search_fields = ('title', 'description')


# Register your models here.
admin.site.register(Task, AdminTask)


#Superuser@123