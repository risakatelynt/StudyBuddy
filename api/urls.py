from django.urls import path
from django.urls import include
from . import views

# app_name = 'user'

urlpatterns = [
    path('', views.loginview, name="login"),
    path('login/', views.loginview, name="login"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('notes/', views.home, name="home"),
     path('note/', views.getNote, name="getNotes"),
    path('createnotes/', views.createNote, name="createnotes"),
    path('deletenotes/', views.deleteNote, name="deletenotes"),
    path('updatenotes/<str:pk>', views.updateNote, name="updatenotes"),
    path('register/', views.register, name="register")
    # path('notes/create/', views.createNote, name="create-note"),
    # path('notes/<str:pk>/update/', views.updateNote, name="update-note"),
    # path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),
    # path('notes/<str:pk>/', views.getNote, name="note")
]
