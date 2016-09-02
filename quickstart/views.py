from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer,ArticleSerializer
from blog.models import Article , User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer