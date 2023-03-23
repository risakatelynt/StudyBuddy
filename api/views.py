from .models import Answer, TagsAndNotes, TagsAndQuestions,Tag,Note,Question, UserProfile
from .serializers import NoteSerializer
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.views import View
from .forms import NoteForm
from rest_framework.response import Response
from django.core.paginator import Paginator
from itertools import chain

# Create your views here.
def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = UserProfile.objects.get(username=username) 
        except:
            messages.error(request,'User does not exist')
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            status_message = {'response' : 'success'}
            return JsonResponse(status_message)
            # return redirect('notes')
        else:
            # If the username or password is incorrect, return an error message
            # error_message = '用户名或密码不正确，请重新输入！'
            status_message = {'response': {'message' : 'username or password is incorrect'}}
            return JsonResponse(status_message)
            # return render(request, 'test.html', {'error_message': error_message})
    else:
        # 如果是 GET 请求，返回空的登录表单
        return render(request, 'login.html')
    
def home(request):
    return render(request, 'notes.html')
    
def register(request):
    if request.method == 'POST':
        # 获取表单数据
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        password2 = request.POST['password2']

        # 校验密码是否一致
        if password == password2:
            # 校验用户名是否已被注册
            if UserProfile.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username already exists'})
            else:
                # 创建新用户
                user = UserProfile.objects.create_user(username=username, password=password, email=email)
                user.save()
                # 注册成功，自动登录并跳转到主页
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                return render(request, 'notes.html')
        else:
            return render(request, 'register.html', {'error': 'The two entered passwords do not match'})
    else:
        return render(request, 'register.html')


def signup(request):
    if request.method == 'POST':
        # 获取表单数据
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        password2 = request.POST['password2']

        # 校验密码是否一致
        if password == password2:
            # 校验用户名是否已被注册
            if UserProfile.objects.filter(username=username).exists():
                # return render(request, 'signup.html', {'error': 'Username already exists'})
                status_message = {'response' : {'message': 'Username already exists'}}
                return JsonResponse(status_message)
            if UserProfile.objects.filter(email=email).exists():
                # return render(request, 'signup.html', {'error': 'Username already exists'})
                status_message = {'response' : {'message': 'email id already exists'}}
                return JsonResponse(status_message)
            else:
                # 创建新用户
                user = UserProfile.objects.create_user(username=username, password=password, email=email)
                user.save()
                # 注册成功，自动登录并跳转到主页
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    status_message = {'response' : 'success'}
                return JsonResponse(status_message)
                # return redirect('notes')
        else:
            # return render(request, 'signup.html', {'error': 'The two entered passwords do not match'})
            status_message = {'response' : {'message': 'The two entered passwords do not match'}}
            return JsonResponse(status_message)
    else:
        return render(request, 'signup.html')
    
'''
def login(request):
    context_dict = {}
    return render(request, 'login.html', context=context_dict)
'''
def createNote(request):
    form = NoteForm()
    # tags = Tag.objects.all()
    if request.method == 'POST':
        # tag_name = request.POST.get('tag')
        # tag, created = Tag.objects.get_or_create(name=tag_name)

        note = Note.objects.create(
            user=request.user,
            # tag=tag,
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            image= request.POST.get('image'),
            rank = request.POST.get('rank'),
        )
        status_message = {'response' : 'success'}
        return JsonResponse(status_message)
        # serializer = NoteSerializer(note, many = False)
        # return Response(serializer.data)
        # return render(request, 'notes.html')
    else:
        return render(request, 'createnotes.html')
    # context = {'form': form, 'tags': tags}
    # return render(request, 'newnoteTest.html', context)

# def getNote(request):
#     if request.method == 'GET':
#         note = Note.objects.all()
#         note_json = serializers.serialize('json', note)
#         notes = [{"image" : "../static/images/image1.png", "title": "Django cautions", "content": "A brief description of the Django frameworks", "rank": "4"},
#                  {"image" : "../static/images/image2.png","title": "Introduction to Django", "content": "Overview of the history of Django has advantages and disadvantages, etc.", "rank": "3"},
#                  {"image" : "../static/images/image3.png","title": "Django's manual", "content": "Some basic teaching of Django", "rank": "3"},
#                  {"image" : "../static/images/jquery.png","title": "jQuery", "content": "How to use jQuery", "rank": "5"}, 
#                  {"image" : "../static/images/frontend.jpg","title": "Frontend", "content": "Introduction to HTML, CSS, JS", "rank": "4"}, 
#                  {"image" : "../static/images/angular.png","title": "Angular", "content": "How to use angular to create a single page application", "rank": "5"},]
#         status_message = {'response' : notes, 'data': note_json}
#         # return render(request, 'notes.html', status_message)
#         return JsonResponse(status_message)

def updateNote(request, pk):
    note = Note.objects.get(id=pk)
    # form = NoteForm(instance=note)
    # tags = Tag.objects.all()
    if request.user != note.user:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        # tag_name = request.POST.get('topic')
        # tag, created = Tag.objects.get_or_create(name=tag_name)
        # note.name = request.POST.get('name')
        # note.tag = tag
        note.title=request.POST.get('title')
        note.content=request.POST.get('content')
        # note.image= request.POST.get('image'),
        note.rank = request.POST.get('rank')
        note.save()
        status_message = {'response' : 'success'}
        return JsonResponse(status_message)

    # context = {'form': form, 'tags': tags, 'note': note}
    return render(request, 'notes.html')

def deleteNote(request, pk):
    note = Note.objects.get(id=pk)

    if request.user != note.user:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'DELETE':
        note.delete()
        status_message = {'response' : 'success'}
        return JsonResponse(status_message)
    return render(request, 'notes.html', {'obj': note})

def newNote(request):
    return render(request, 'newNote.html')

# 分页显示所有笔记/Show all notes in pages
def notes_lists(request):
    if request.method == "GET":
        all_notes = Note.objects.all()
        # paginator = Paginator(all_notes, 10)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        page_json = serializers.serialize('json', all_notes)
        # note_json = serializers.serialize('json',  all_notes)
        # return render(request, "notes.html", {
        #     'page_obj': page_obj,
        #     "questions": all_notes
        # })
        return JsonResponse( {'page_obj': page_json})

# 写笔记/Writing notes
def write_note(request):
    if request.method == "POST":
        form_data = request.POST
        userId = form_data.POST.get('user_id')
        noteContent = form_data.POST.get('content')
        tagId = form_data.POST("tag_id")
        note = Note()
        note.user_id = userId
        note.content = noteContent
        note.tag_id = tagId
        note.save()
        return render(request, "notes.html", {
            'state': 'success',
        })

# 点击查看笔记详情/Click for details of notes
def noteDetail(request, pk):
    if request.method == "GET":
        # noteId = request.GET.get(pk)
        note = Note.objects.get(id=pk)
        # page_json = serializers.serialize('json', note)
        # return render(request, "notes", {
        #     'note': note,
        # })
        # serializer = NoteSerializer(note, many = False)
        return JsonResponse({'page_obj': note})

# 点击为笔记打分/Click to rate the notes
def rateNote(request):
    if request.method == "POST":
        form_data = request.POST
        noteId = form_data.POST.get('note_id')
        noteRank = form_data.POST.get('rank')
        print("get id=" + noteId)
        note = Note.objects.get(pk=noteId)
        note.rank = noteRank
        note.save()
        return render(request, "notes.html", {
            'state': 'success',
        })

# 点击显示标签下的笔记/Click to show notes under the tab
def tagNotes(request):
    if request.method == "GET":
        tag_id = request.GET.get('tag_id')
        tagAndNotes = TagsAndNotes.objects.filter(tag_id = tag_id)
        all_tagNotes = tagAndNotes.all()
        all_notes = []
        for tagNote in all_tagNotes:
            new_note = Note.objects.get(pk = tagNote.note_id)
            all_notes.append(new_note)
        paginator = Paginator(all_notes, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "notes.html", {
            'page_obj': page_obj,
            "notes": all_notes
        })

# 对笔记名称和内容进行模糊查找/Fuzzy search for note titles and content
def searchNotes(request):
    if request.method == "GET":
        keyword = request.GET.get('keyword')
        print("get keyword=" + keyword)
        note1 = Note.objects.filter(title__contains=keyword)
        note2 = Note.objects.filter(content__contains=keyword)
        note = list(chain(note1,note2))
        return render(request, "notes.html", {
            'note': note,
        })


def allQuestions(request):
    if request.method == "GET":
        all_questions = Question.objects.all()
        paginator = Paginator(all_questions, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # return render(request, "notes.html", {
        #     'page_obj': page_obj,
        #     "questions": all_questions
        # })
        question_json = serializers.serialize('json', all_questions)
        page_json =serializers.serialize('json', page_obj)
        return JsonResponse( {"questions": question_json, "page_obj": page_json})
    # else: 
    #     return render(request, "questions.html")

# 点击显示问题细节内容/Click to show details of the problem
def questionDetail(request, questionId):
    if request.method == "GET":
        # questionId = request.GET.get('question_id')
        # print("get id=" + questionId)
        question = Question.objects.get(pk=questionId)
        answers = Answer.objects.filter(question_id=questionId)
        max = -1
        for answer in answers:
            if answer.rank > max:
                best_answer = answer
            max = best_answer.rank
        # return render(request, "questions.html", {
        #     'question': question,
        #     'best_answer': best_answer
        # })
        # json =serializers.serialize('json', page_obj)
        return JsonResponse( {'question': question, 'best_answer': best_answer})

# 回答问题/Answering questions
def answerQuestion(request):
    if request.method == "POST":
        form_data = request.POST
        question_id = form_data.POST.get('question_id')
        user_id = form_data.POST.get('user_id')
        answer_content = form_data.POST.get('answer')
        question = Question.objects.get(pk=question_id)
        question.user_id = user_id
        answer = Answer();
        answer.user_id = user_id
        answer.content = answer_content
        answer.question_id = question_id
        answer.save()
        question.save()
    return render(request, "questions.html", {
        'state': 'success',
    })

# 点击显示标签下的问题/Click to show issues under the tab
def tagQuestions(request):
    if request.method == "GET":
        tag_id = request.GET.get('tag_id')
        tagAndQuestions = TagsAndQuestions.objects.filter(tag_id = tag_id)
        all_tagQuestions = tagAndQuestions.all()
        all_questions = []
        for tagQuestion in all_tagQuestions:
            new_question = Question.objects.get(pk = tagQuestion.question_id)
            all_questions.append(new_question)
        paginator = Paginator(all_questions, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "questions.html", {
            'page_obj': page_obj,
            "questions": all_questions
        })

# 显示全部标签/Show all tags
def allTag(request):
    if request.method == "GET":
        all_tags = Tag.objects.all()
        return render(request, "questions.html", {
            "tag":all_tags
        })


# 对问题名称进行模糊查找/Fuzzy search for questions titles and content
def searchNotes(request):
    if request.method == "GET":
        keyword = request.GET.get('keyword')
        print("get keyword=" + keyword)
        questions1 = Question.objects.filter(title__contains=keyword)
        questions2 = Question.objects.filter(content__contains=keyword)
        questions = list(chain(questions1, questions2))
        return render(request, "notes.html", {
            'questions': questions,
        })

def allTags(request):
    if request.method == "GET":
        all_tag = Tag.objects.all()
        return render(request, "questions.html", {
            'tags':all_tag,
        })