from utils.serializers import BaseSerializer, BaseListPageSerializer


class WorksSerializer(BaseSerializer):
    """ 作品的详细信息 """

    def to_dict(self):  # 重写
        obj = self.obj
        return {
            'id': obj.pk,
            'user': obj.user.nickname,
            'name': obj.name,
            'desc': obj.desc,
            'coverImg': obj.coverImg_url,  # 封面图地址
            'mainImg': obj.mainImg_url,
            'avatar': obj.user.avatar_url,
            'types': obj.types,
            'score': obj.score,
            'origin': obj.origin,
            'love_counts': obj.love_counts,  # 点赞总数
            'counts': obj.comments.count(),  # 评论总数

        }


class WorkListSerializer(BaseListPageSerializer):
    """ 作品列表 """
    def get_object(self, obj):
        return {
            'id': obj.pk,
            'user': obj.user.nickname,
            'name': obj.name,
            'coverImg': obj.coverImg_url,  # 封面图地址
            'avatar': obj.user.avatar_url,
            'types': obj.types,
            'score': obj.score,
            'origin': obj.origin,
            'love_counts': obj.love_counts,
            'comment_count': obj.comments.count(),
        }


class CommentListSerializer(BaseListPageSerializer):
    """ 评论列表 """

    def get_object(self, obj):#
        user = obj.user
        return {
            'user': {
                'pk': user.pk,
                'avatar': user.avatar_url,
                'nickname': user.nickname
            },
            'pk': obj.pk,
            'content': obj.content,
            'is_top': obj.is_Top,
            'love_counts': obj.love_counts,
            'score': obj.score,
        }