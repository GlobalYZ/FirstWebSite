from utils.serializers import BaseSerializer, BaseListPageSerializer


class WorksSerializer(BaseSerializer):
    """ 作品的详细信息 """

    def to_dict(self):  # 重写
        artwork = self.obj
        return {
            'id': artwork.pk,
            'auth': artwork.user.nickname,
            'name': artwork.name,
            'desc': artwork.desc,
            'coverImg': artwork.coverImg_url,  # 封面图地址
            'mainImg': artwork.mainImg_url,
            'types': artwork.types,
            'origin': artwork.origin,
            'counts': artwork.comments.count(),  # 评论总数
            'love_counts': artwork.lovecounts.count(),  # 点赞总数
        }


class WorkListSerializer(BaseListPageSerializer):
    """ 作品列表 """
    def get_object(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'mainImg': obj.mainImg.url,
            'user': obj.user,
            'types': obj.types,
            'score': obj.score,
            'origin': obj.origin,
            'comment_count': obj.comment_count,
        }
