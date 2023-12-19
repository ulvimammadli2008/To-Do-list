from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='task'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='taskdetail'),
    path('create-task/', TaskCreate.as_view(), name='taskcreate'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='taskupdate'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='taskdelete'),


]