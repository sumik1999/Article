from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model, authenticate

from post.models import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['title','description','created_at','author']
