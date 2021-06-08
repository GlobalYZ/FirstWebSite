# Generated by Django 3.2 on 2021-06-07 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import works.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('desc', models.CharField(blank=True, max_length=1000, null=True, verbose_name='描述')),
                ('origin', models.SmallIntegerField(choices=[(0, '原创'), (1, '转发')], default=0, verbose_name='作品来源')),
                ('coverImg', models.ImageField(blank=True, default='avatar/default.jpeg', null=True, upload_to=works.models.set_cover, verbose_name='封面图')),
                ('mainImg', models.ImageField(blank=True, default='avatar/default.jpeg', null=True, upload_to=works.models.set_main, verbose_name='主图')),
                ('types', models.SmallIntegerField(choices=[(0, '搞笑类'), (1, '其它类')], default=0, verbose_name='展现的类型')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='生效开始时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='生效结束的时间')),
                ('target_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='跳转的地址')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art_work', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '作品表',
                'verbose_name_plural': '作品表',
                'db_table': 'works_artwork',
                'ordering': ['name'],
            },
        ),
    ]
