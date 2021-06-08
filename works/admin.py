from django.contrib import admin
from utils.actions import set_invalid, set_valid
from works.models import Artwork
from accounts.models import User


@admin.register(Artwork)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_valid', 'created_at', 'created_at')
    fieldsets = (
        ('基本数据', {
            'fields': ['name', 'desc', 'coverImg', 'mainImg', 'types', 'user'],
            'classes': ('wide', 'extrapretty'),
        }),
        ('其他', {
            'fields': ['start_time', 'end_time'],
            'classes': ('wide', 'extrapretty'),
        }),
    )
    search_fields = ('user__username', )
    actions = [set_invalid, set_valid]