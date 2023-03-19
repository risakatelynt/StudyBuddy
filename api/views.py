from .models import User
from .serializers import NoteSerializer
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

# Create your views here.
def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username) 
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
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username already exists'})
            else:
                # 创建新用户
                user = User.objects.create_user(username=username, password=password, email=email)
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
            if User.objects.filter(username=username).exists():
                # return render(request, 'signup.html', {'error': 'Username already exists'})
                status_message = {'response' : {'message': 'Username already exists'}}
                return JsonResponse(status_message)
            if User.objects.filter(email=email).exists():
                # return render(request, 'signup.html', {'error': 'Username already exists'})
                status_message = {'response' : {'message': 'email id already exists'}}
                return JsonResponse(status_message)
            else:
                # 创建新用户
                user = User.objects.create_user(username=username, password=password, email=email)
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
def notes(request):
    context_dict = {}
    return render(request, 'notes.html', context=context_dict)


