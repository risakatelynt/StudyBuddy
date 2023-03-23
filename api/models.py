from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True
'''
class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return first 50 characters
        return self.body[0:50]
'''

class UserProfile(AbstractUser):
    # userId = models.UUIDField(primary_key=True)
    nick_name = models.CharField(max_length=50, null=True,blank=True)
    address = models.CharField(max_length=100,default="",null=True,blank=True)
    mobile = models.CharField(max_length=11,unique=True,null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    image = models.ImageField(upload_to="head_image/%Y/%m", default="default.jpg",null=True,blank=True)


    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = verbose_name

    def __str__(self):
       if self.nick_name:
           return self.nick_name
       else:
           return self.username
    
class Note(BaseModel):
    # noteId = models.UUIDField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    rank = models.IntegerField(default=0)
    content = models.TextField()
    image = models.ImageField(upload_to="notes/%y/%m", max_length=100, default="default.jpg")

    class Meta:
        verbose_name = "Note"


class Question(models.Model):
    # questionId = models.UUIDField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    rank = models.IntegerField(default=0)
    content = models.TextField()
    add_time = models.DateTimeField(default=datetime.now)

class Tag(BaseModel):
    name = models.CharField(max_length=50, null=True,blank=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = verbose_name



class Answer(models.Model):
    # questionId = models.UUIDField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    content = models.TextField()
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Answer"


        
class TagsAndQuestions(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "TagsAndQuestions"

class TagsAndNotes(BaseModel):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "TagsAndNotes"





