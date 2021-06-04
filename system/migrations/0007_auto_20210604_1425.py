# Generated by Django 3.2 on 2021-06-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20210604_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['number'], 'verbose_name': '轮播图', 'verbose_name_plural': '轮播图'},
        ),
        migrations.AlterField(
            model_name='slider',
            name='types',
            field=models.SmallIntegerField(choices=[(0, '轮播图'), (1, '展示图')], default=0, verbose_name='展现的位置'),
        ),
    ]