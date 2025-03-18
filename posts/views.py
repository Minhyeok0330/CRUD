from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)    

    context =  {
        'post' : post,
    }

    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
#필요한 데이터 추출
    post = Post()
    post.title = title
    post.content = content
#DB에 저장
    post.save()

    #return redirect('/index/')
    return redirect(f'/posts/{post.id}/')

    