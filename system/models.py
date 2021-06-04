from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from accounts.models import User
from utils.models import CommonModel


class Slider(CommonModel):
    """ 轮播图 """
    IMG_CHOICES = (
        (0, '轮播图'),
        (1, '展示图'),
    )
    name = models.CharField('名称', max_length=32)
    desc = models.CharField('描述', max_length=100, null=True, blank=True)
    types = models.SmallIntegerField('展现的位置', choices=IMG_CHOICES, default=0)
    img = models.ImageField('图片地址', max_length=255, upload_to='slider')
    number = models.SmallIntegerField('排序字段', default=0, help_text="默认为升序排列")
    start_time = models.DateTimeField('生效开始时间', null=True, blank=True)
    end_time = models.DateTimeField('生效结束的时间', null=True, blank=True)
    target_url = models.CharField('跳转的地址', max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'system_slider'
        ordering = ['number']
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'

    def __str__(self):
        return self.name


class ImageRelated(CommonModel):
    """ 图片关联 """
    img = models.ImageField('图片', upload_to='%Y%m/file/', max_length=256)
    summary = models.CharField('图片说明', max_length=32, null=True, blank=True)
    user = models.ForeignKey(User,
                             on_delete=models.SET(None),
                             related_name='upload_images',
                             verbose_name='上传的用户',
                             null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField('关联的模型')
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'system_image_related'


class Questions(CommonModel):
    number = models.SmallIntegerField('编号', default=1, help_text='默认为升序排列')
    title = models.CharField('问题', max_length=100, null=True, blank=True)
    desc = models.TextField(verbose_name='描述', null=True, blank=True)

    class Meta:
        db_table = 'system_questions'
        ordering = ['number']
        verbose_name = '常见问题'
        verbose_name_plural = '常见问题'

    def __str__(self):
        return self.title
