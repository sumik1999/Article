from django.shortcuts import render
from rest_framework import  authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class CreatePostApi(APIView):
    """ A view to create a new post for an authenticated user"""

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            post = serializer.save(author=request.user)
            print(post)
            serializer = PostSerializer(post)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ListPostApi(APIView):
    """A view to list all posts whose author is the current user"""

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user
        posts = Post.objects.filter(author=user)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeletePostApi(APIView):
    """A view to delete a post by id if its author is the current logged in user"""

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self,request,id):
        post = Post.objects.filter(id=id)
        
        if (post and request.user==post.author):
            Post.objects.remove(id=id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(message="post with the given id not found or the user isn't the author",status=status.HTTP_400_BAD_REQUEST)


class UpdatePostApi(APIView):
    """A view to update a post by its id if the user is the author of the post"""

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def patch(self,request,id):
        data = request.data
        post = Post.objects.filter(id=id)
        if (post and request.user==post.author):
            serializer = PostSerializer(post, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrievePostApi(APIView):
    """A view to get a particular post by id of the current user only"""

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,id):
        post = Post.objects.filter(id=id)
        if (post and request.user==post.author):
            serializer = PostSerializer(post)
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

















    





# Create your views here.
