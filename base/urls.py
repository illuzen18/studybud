from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('roomform/', views.createRoom, name="roomform"),
    path('updateroom/<str:pk>/', views.updateRoom, name="updateroom"),
    path('deleteroom/<str:pk>/', views.deleteRoom, name="deleteroom"),
    path('deletemessage/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('update-user.html', views.updateUser, name="update-user"),
    path('topics.html',views.topicsPage, name="topics-page")


]
