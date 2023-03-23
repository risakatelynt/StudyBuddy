from django.contrib import admin

# Register your models here.

from .models import Note,UserProfile,Question,Tag,TagsAndNotes,TagsAndQuestions

admin.site.register(Note)
admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(TagsAndNotes)
admin.site.register(TagsAndQuestions)