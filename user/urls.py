
from django.urls import path, include
from .views import CreateTokenView, CreateUserView, DeleteUpdateRetrieveUserView, ListUserView


urlpatterns = [
    # route to create a new user
    path("create/", CreateUserView.as_view(), name="create"),
    # route to get the token for a user with valid username and password
    path("token/", CreateTokenView.as_view(), name="token"),
    # route to update/delete/retrieve an user
    path("<int:pk>/", DeleteUpdateRetrieveUserView.as_view()),
    # route to list all users
    path("list/", ListUserView.as_view())

]
