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
    path('createnotes/', views.createNote, name="createNote"),
    path('note/', views.notes_lists, name="notes_lists"),
    path('deletenotes/<str:pk>', views.deleteNote, name="deletenotes"),
    # path('note/<str:pk>', views.noteDetail, name="noteDetail"),
    path('updatenotes/<int:pk>', views.updateNote, name="updatenotes"),
    path('register/', views.register, name="register"),
    path('questions/', views.allQuestions, name="allQuestions"),
    path('questionDetail/<str:pk>', views.questionDetail, name="questionDetail"),
   
    # path('notes/create/', views.createNote, name="create-note"),
    # path('notes/<str:pk>/update/', views.updateNote, name="update-note"),
    # path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),
    # path('notes/<str:pk>/', views.getNote, name="note")
]
