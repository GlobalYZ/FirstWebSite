from django.utils.translation import gettext_lazy as _ # 用于下面的 'GlobalYZ后台管理系统'
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include,url
from django.conf import settings
from django.views.static import serve# 指向静态文件存放地址的规则

urlpatterns = [
    path('admin/', admin.site.urls),
    # 系统模块
    path('system/', include('system.urls')),
    # 用户账户模块
    path('accounts/', include('accounts.urls')),
]

'''下面是Django框架提供的一个内置视图，可以按照它给定的规则进行配置，在开发的时候把项目当中的静态文件放到Django的内置服务器当中，
    使可直接进行访问，但不满足生产需要'''
# http://127.0.0.1:8000/media/avatar/202106/111.jpeg/ 访问即可看到图片
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$',serve,{
            'document_root': settings.MEDIA_ROOT,
        }),
        # path('__debug__/',include(debug_toolbar.urls)),
    ]

admin.site.site_header = _('GlobalYZ的网站后台')