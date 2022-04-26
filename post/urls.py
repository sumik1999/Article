from django.urls import path
from .views import ListPostApi,CreatePostApi, DeletePostApi,UpdatePostApi,RetrievePostApi

urlpatterns = [
    
    path('',ListPostApi.as_view()),
    path('create/',CreatePostApi.as_view()),
    path('<int:id>/update/',UpdatePostApi.as_view()),
    path('<int:id>/delete/',DeletePostApi.as_view()),
    path('<int:id>/retrieve/',RetrievePostApi.as_view()),
]