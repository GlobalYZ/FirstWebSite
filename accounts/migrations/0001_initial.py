# Generated by Django 3.2 on 2021-06-10 10:46

import accounts.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(blank=True, default='avatar/default.jpeg', null=True, upload_to=accounts.models.set_avatar, verbose_name='用户头像')),
                ('nickname', models.CharField(max_length=32, unique=True, verbose_name='昵称')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'account_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(editable=False, max_length=64, unique=True, verbose_name='用户名')),
                ('real_name', models.CharField(max_length=32, verbose_name='真实姓名')),
                ('email', models.CharField(blank=True, max_length=128, null=True, verbose_name='电子邮箱')),
                ('is_email_valid', models.BooleanField(default=False, verbose_name='邮箱是否已经验证')),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号码')),
                ('is_phone_valid', models.BooleanField(default=False, verbose_name='是否已经验证')),
                ('sex', models.SmallIntegerField(choices=[(1, '男'), (0, '女')], default=1, verbose_name='性别')),
                ('age', models.SmallIntegerField(default=0, verbose_name='年龄')),
                ('sign', models.CharField(blank=True, max_length=128, null=True, verbose_name='签名')),
                ('source', models.CharField(max_length=16, null=True, verbose_name='登录的来源')),
                ('version', models.CharField(max_length=16, null=True, verbose_name='登录的版本')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户详细信息',
                'verbose_name_plural': '用户详细信息',
                'db_table': 'accounts_user_profile',
            },
        ),
        migrations.CreateModel(
            name='LoginRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='登录的账号')),
                ('ip', models.CharField(max_length=32, verbose_name='IP')),
                ('address', models.CharField(blank=True, max_length=32, null=True, verbose_name='地址')),
                ('source', models.CharField(max_length=16, null=True, verbose_name='登录的来源')),
                ('version', models.CharField(max_length=16, null=True, verbose_name='登录的版本')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登录时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='login_records', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户登录日志',
                'verbose_name_plural': '用户登录日志',
                'db_table': 'accounts_login_record',
            },
        ),
    ]
