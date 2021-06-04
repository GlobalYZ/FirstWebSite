from django.contrib import admin

from system.models import Questions, Slider
from utils.actions import set_invalid, set_valid


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'is_valid', 'created_at', 'created_at')
    fieldsets = (('', {
        'fields': ['number', 'title', 'desc'],
        'classes': ('wide', 'extrapretty'),
    }),)
    actions = [set_invalid, set_valid]


@admin.register(Slider)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'is_valid', 'created_at', 'created_at')
    fieldsets = (
        ('基本数据', {
            'fields': ['number', 'name', 'desc', 'img', 'types', 'target_url'],
            'classes': ('wide', 'extrapretty'),
        }),
        ('其他', {
            'fields': ['start_time', 'end_time'],
            'classes': ('wide', 'extrapretty'),
        }),
    )
    actions = [set_invalid, set_valid]
