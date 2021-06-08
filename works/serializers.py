from utils.serializers import BaseSerializer

class WorksSerializer(BaseSerializer):
    """ 作品的详细信息 """
    def to_dict(self):# 重写
        artwork = self.obj
        return {
            'id': artwork.pk,
            'name': artwork.name,
            'desc': artwork.desc,
            'coverImg': artwork.coverImg_url,# 封面图地址
            'mainImg': artwork.mainImg_url,
            'types': artwork.types,
        }