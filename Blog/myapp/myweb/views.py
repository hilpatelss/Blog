from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from myweb.models import *

def home(request):
    if request.method == "POST":
        b_title =request.POST.get('link')
        data = Blog.objects.get(b_title=b_title)
        return redirect('read',data = data.id)
    
    blog = Blog.objects.all()
    context = {'page': 'Home', 'blog':blog}
    return render(request , "home.html", context)


def read(request,data):
    querset = Blog.objects.get(id=data)
    context = {'page': 'Home', 'blog':querset}
    return render(request , "read.html", context)

@login_required(login_url="/signup/")    
def blog(request):
    if request.method =='POST':
        b_file = request.POST.get('b_file')
        b_title = request.POST.get('b_title')
        b_heading =  request.POST.get('b_heading')
        b_blog = request.POST.get('b_blog')
        
        blog = Blog.objects.create(
            b_img = b_file,
            b_title = b_title,
            b_heading =  b_heading,
            b_blog = b_blog
        )
        blog.save()
        return redirect('home')    
    context = {'page': 'blog'}
    return render(request , "blog.html", context)


def signin(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, 'invalid Username')
            return redirect('/signin/')
        
        user = authenticate(username =username,password =password)
        
        if User is None:
            messages.info(request, 'invalid password')
            return redirect('/signin/')
        
        else:
            login(request ,user)
            return redirect('home')
        
            
    context = {'page': 'signin'}
    return render(request , "signin.html", context)
def signup(request):
    
    if request.method =="POST":
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        email = request.POST.get('email')        
        username = request.POST.get('username')
        password = request.POST.get('password')

        if len(first_name) == 0 or len(last_name) == 0 or len(email) == 0 or len(username)==0 or len(password) == 0 :
            messages.info(request, 'fild cant be empty')
            return redirect('/signup/')
        
        user= User.objects.filter(username = username)
        if  user.exists() :
            messages.info(request, 'User name is alraedy taken')
            return redirect('/signup/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
        )
        user.set_password(password)
        user.save() 
        login(request ,user)
       
       
        
            
        return redirect('home')
    
    context = {'page': 'signup'}
    return render(request , "signup.html", context)

@login_required(login_url="home")
def signout(request):
    logout(request)
    return redirect('home')
