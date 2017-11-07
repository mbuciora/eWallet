from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ChangeDetail
from .models import Group
from .models import GroupChange
from .models import User
from .models import UserChange
from .models import UserGroup
from .serializers import ChangeDetailSerializer
from .serializers import GroupChangeSerializer
from .serializers import GroupSerializer
from .serializers import UserChangeSerializer
from .serializers import UserGroupSerializer
from .serializers import UserSerializer


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username, password=password)
        if user.exists():
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)


class GroupList(APIView):
    def get(self, request):
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)


class UserGroupList(APIView):
    def get(self, request):
        userGroup = UserGroup.objects.all()
        serializer = UserGroupSerializer(userGroup, many=True)
        return Response(serializer.data)


class ChangeDetailList(APIView):
    def get(self, request):
        changeDetail = ChangeDetail.objects.all()
        serializer = ChangeDetailSerializer(changeDetail, many=True)
        return Response(serializer.data)


class GroupChangeList(APIView):
    def get(self, request):
        groupChange = GroupChange.objects.all()
        serializer = GroupChangeSerializer(groupChange, many=True)
        return Response(serializer.data)


class UserChangeList(APIView):
    def get(self, request):
        userChange = UserChange.objects.all()
        serializer = UserChangeSerializer(userChange, many=True)
        return Response(serializer.data)
