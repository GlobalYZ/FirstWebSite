from django.db import transaction
from django import forms

from accounts.models import User
from works.models import Artwork


class WorksForm(forms.Form):
    username = forms.CharField(label='手机号码', max_length=16, required=True, error_messages={'required': '请输入手机号码'})
    name = forms.CharField(label='名称', max_length=32, required=False, error_messages={'required': '描述需要更改'})
    desc = forms.CharField(label='描述', max_length=1000, required=False, error_messages={'required': '描述需要更改'})
    coverImg = forms.ImageField(label='封面图', required=False, error_messages={'required': '图片不可用'})
    mainImg = forms.ImageField(label='主图', required=False, error_messages={'required': '图片不可用'})
    types = forms.IntegerField(label='类型', required=False, error_messages={'required': '类型有误'})

    @transaction.atomic
    def upload(self, request):
        """ 上传信息 """
        data = self.cleaned_data
        username = data['username']
        name = data['name']
        desc = data['desc']
        coverImg = request.FILES.get('coverImg', '')
        mainImg = request.FILES.get('mainImg', '')
        types = data['types']
        version = request.headers.get('version', '')
        source = request.headers.get('source', '')
        ip = request.META.get('REMOTE_ADDR', '')
        try:
            user = User.objects.get(username=username)
            artwork = Artwork.objects.create(
                name=name, desc=desc, coverImg=coverImg, mainImg=mainImg, types=types, user=user
            )
            user.save()
            user.add_login_record(username=user.username, ip=ip, source=source, version=version)
            return user, artwork
        except Exception as e:
            print(e)
            return None