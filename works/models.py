from django.db import models

from accounts.models import User
from utils.models import CommonModel


def set_cover(artwork, filename):
    return 'works/{username}/{filename}'.format(username=artwork.user.username, filename=filename)


def set_main(artwork, filename):
    return 'works/{username}/{filename}'.format(username=artwork.user.username, filename=filename)


class Artwork(CommonModel):
    """ 作品表 """
    IMG_CHOICES = (
        (0, '搞笑类'),
        (1, '其它类'),

    )
    ORI_CHOICES = (
        (0, '原创'),
        (1, '转发'),
    )
    name = models.CharField('名称', max_length=32)
    desc = models.CharField('描述', max_length=1000, null=True, blank=True)
    origin = models.SmallIntegerField('作品来源', choices=ORI_CHOICES, default=0)
    coverImg = models.ImageField('封面图', upload_to=set_cover,
                                 null=True, blank=True, default='avatar/default.jpeg')
    mainImg = models.ImageField('主图', upload_to=set_main,
                                null=True, blank=True, default='avatar/default.jpeg')
    types = models.SmallIntegerField('展现的类型', choices=IMG_CHOICES, default=0)
    start_time = models.DateTimeField('生效开始时间', null=True, blank=True)
    end_time = models.DateTimeField('生效结束的时间', null=True, blank=True)
    score = models.FloatField('评分', default=5)
    user = models.ForeignKey(User, related_name='art_work', on_delete=models.CASCADE)

    @property
    def comment_count(self):
        """ 评论总数 """
        return self.comments.filter(is_valid=True).count()

    @property
    def coverImg_url(self):
        return self.coverImg.url if self.coverImg else ''

    @property
    def mainImg_url(self):
        return self.mainImg.url if self.mainImg else ''

    class Meta:
        db_table = 'works_artwork'
        ordering = ['name']
        verbose_name = '作品表'
        verbose_name_plural = '作品表'
    def __str__(self):
        return self.name


class Comment(CommonModel):
    """ 评论及回复 """
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, verbose_name='评论人')
    artwork = models.ForeignKey(Artwork, related_name='comments', on_delete=models.CASCADE, verbose_name='评论的作品')
    content = models.TextField(verbose_name='评论的内容', blank=True, null=True)
    is_Top = models.BooleanField(verbose_name='是否置顶', default=False)
    love_count = models.IntegerField(verbose_name='点赞次数', default=0)
    score = models.FloatField(verbose_name='评分', default=5)
    ip_address = models.CharField(verbose_name='IP地址', blank=True, null=True, max_length=64)

    class Meta:
        db_table = 'works_comment'
        ordering = ['-love_count', '-created_at']
        verbose_name = '评论及回复'
        verbose_name_plural = '评论及回复'

    def __str__(self):
        return self.content

class LoveCount(CommonModel):
    """ 点赞 """
    user = models.ForeignKey(User, related_name='lovecounts', on_delete=models.CASCADE, verbose_name='点赞人')
    artwork = models.ForeignKey(Artwork, related_name='lovecounts', on_delete=models.CASCADE, verbose_name='点赞的作品')
    count = models.IntegerField(verbose_name='点赞次数', default=0)

    class Meta:
        db_table = 'works_lovecount'
        ordering = ['-count', '-created_at']
        verbose_name = '点赞'
        verbose_name_plural = '点赞'

    def __str__(self):
        return self.artwork.name