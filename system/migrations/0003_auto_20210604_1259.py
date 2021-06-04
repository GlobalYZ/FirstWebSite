# Generated by Django 3.2 on 2021-06-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_questions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'verbose_name': '常见问题', 'verbose_name_plural': '常见问题'},
        ),
        migrations.AlterField(
            model_name='questions',
            name='desc',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='描述'),
        ),
    ]