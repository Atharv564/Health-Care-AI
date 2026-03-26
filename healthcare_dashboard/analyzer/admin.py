from django.contrib import admin
from .models import HealthReport

@admin.register(HealthReport)
class HealthReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'created_at')  # fields to show in admin list
    list_filter = ('created_at', 'user')          # filters in admin sidebar
    search_fields = ('user__username',)           # search by username