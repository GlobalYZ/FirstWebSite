from django.contrib import admin
from utils.actions import set_invalid, set_valid
from works.models import Artwork, Comment, LoveCount
from accounts.models import User


@admin.register(Artwork)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_valid', 'created_at', 'created_at')
    fieldsets = (
        ('基本数据', {
            'fields': ['name', 'desc', 'coverImg', 'mainImg', 'types', 'origin', 'user'],
            'classes': ('wide', 'extrapretty'),
        }),
        ('其他', {
            'fields': ['start_time', 'end_time'],
            'classes': ('wide', 'extrapretty'),
        }),
    )
    search_fields = ('user__username', )
    actions = [set_invalid, set_valid]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('format_username', 'format_workname', 'is_valid', 'created_at', 'created_at')
    fieldsets = (
        ('基本数据', {
            'fields': ['user', 'artwork', 'love_count', 'is_Top', 'content', 'score'],
            'classes': ('wide', 'extrapretty'),
        }),
        ('其他', {
            'fields': ['ip_address'],
            'classes': ('wide', 'extrapretty'),
        }),
    )
    search_fields = ('user__username', )
    def format_username(self, obj):
        return obj.user.nickname
    format_username.short_description = '用户昵称'
    def format_workname(self, obj):
        return obj.artwork.name
    format_workname.short_description = '作品名称'
    actions = [set_invalid, set_valid]



@admin.register(LoveCount)
class LoveCountAdmin(admin.ModelAdmin):
    list_display = ('count', 'format_username', 'format_workname', 'is_valid', 'created_at', 'created_at')
    fieldsets = (
        ('基本数据', {
            'fields': ['user', 'artwork', 'count'],
            'classes': ('wide', 'extrapretty'),
        }),
    )
    search_fields = ('user__username', )
    def format_username(self, obj):
        return obj.user.nickname
    format_username.short_description = '用户昵称'
    def format_workname(self, obj):
        return obj.artwork.name
    format_workname.short_description = '作品名称'
    actions = [set_invalid, set_valid]