from utils.serializers import BaseSerializer, BaseListPageSerializer

class UserSerializer(BaseSerializer):
    """ 用户的基础信息 """
    def to_dict(self):# 重写
        user = self.obj
        return {
            'id': user.pk,
            'username': user.username,
            'nickname': user.nickname,
            'avatar': user.avatar_url,# 头像地址
            'email': user.email,
        }

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
            'types': obj.IMG_CHOICES[obj.types][1],
            'score': obj.score,
            'origin': obj.ORI_CHOICES[obj.origin][1],
            'love_counts': obj.love_counts,  # 点赞总数
            'counts': obj.comments.count(),  # 评论总数

        }

class CommentSerializer(BaseSerializer):
    """ 评论成功的返回信息 """
    def to_dict(self):# 重写
        comment = self.obj
        return {
            'pk': comment.artwork.pk,
            'id': comment.user.pk,
            'username': comment.user.username,
            'nickname': comment.user.nickname,
            'avatar': comment.user.avatar_url,# 头像地址
            'score': comment.score,
            'time': comment.created_at,
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
            'types': obj.IMG_CHOICES[obj.types][1],
            'score': obj.score,
            'origin': obj.ORI_CHOICES[obj.origin][1],
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
            'time': obj.created_at,
        }