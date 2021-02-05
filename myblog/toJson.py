# 数据的序列化 将models表中的数据变成json格式
from rest_framework import serializers
from myblog.models import Classes, UserInfo


class Classes_data(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Classes
        fields = '__all__'


class UserInfo_data(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = UserInfo
        fields = '__all__'
