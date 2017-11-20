from rest_framework import serializers
from .models import User
from .models import Group
from .models import UserGroup
from .models import ChangeDetail
from .models import GroupChange
from .models import UserChange


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # ZMIANA


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'


class ChangeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeDetail
        fields = '__all__'


class GroupChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChange
        fields = '__all__'


class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChange
        fields = '__all__'
