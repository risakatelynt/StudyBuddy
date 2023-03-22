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

class User(AbstractUser):
    username = models.CharField(max_length=200, null=True,unique=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=6, null=True)
    
    def __str__(self):
        return self.username
    
class Tag(BaseModel):
    name = models.CharField(max_length=50, null=True,blank=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name
    
class Note(BaseModel):
    # noteId = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50,null=True)
    rank = models.IntegerField(default=0)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="notes/%y/%m", max_length=100,default="default.jpg")

    class Meta:
        verbose_name = "Note"
    def __str__(self):
        # return first 50 characters
        return self.title

class Question(BaseModel):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    rank = models.IntegerField(default=0)
    content = models.TextField()
    

    class Meta:
        verbose_name = "Question"
    def __str__(self):
        return self.title



''' 
class TagsAndNotes(BaseModel):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    notes = models.ForeignKey(Note,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "TagsAndNotes"
    
class TagsAndQuestions(BaseModel):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "TagsAndQuestions"
'''