from django.utils.translation import gettext_lazy as _ # 用于下面的 'GlobalYZ后台管理系统'
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    # 系统模块
    path('system/', include('system.urls')),
    # 用户账户模块
    path('accounts/', include('accounts.urls')),
]



admin.site.site_header = _('GlobalYZ的网站后台')