from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'category', 'date_of_incident', 'timestamp')
    list_filter = ('category', 'date_of_incident')
    search_fields = ('student_id', 'full_name', 'description')
    readonly_fields = ('timestamp',)