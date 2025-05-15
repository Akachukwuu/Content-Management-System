from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post

#All comments below were written by me for future clarity purpose


#The base page
def index(request):
    return render(request, 'index.html')

#Homepage after user is logged in
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

#User registration
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This user already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in Use')
                return redirect('register')
            else: 
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Details')
    return render(request, 'login.html')


#user creates content

def create_content(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        create_post = Post.objects.create(title=title, body=body)
        if create_post is not None:
            create_post.save()
        else:
            messages.info(request, 'Field cannot be left empty')
            return redirect('create_content')
    return render(request, 'create_content.html')

#Displays full blog page when a user clicks on the blog snippet
def display_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'display_post.html', {'post':post})


def logout_user(request):
    logout(request)
    return redirect('login')




#takes user input post title, body
#stores it in the database
#its automatically updated