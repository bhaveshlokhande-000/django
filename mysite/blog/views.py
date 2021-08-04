from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.

@login_required
def home(request):
    
    id=get_current_user_id(request)
    
    all_posts=Post.new_manager.all()

    p=Paginator(all_posts,2)

    page=p.page(1)

    return render(request,'index.html',{'posts':page, "current_user_id":id})


@login_required
def paginate(request,index):
    
    id=get_current_user_id(request)
    
    all_posts=Post.new_manager.all()

    p=Paginator(all_posts,5)
    
    try:
        page=p.page(index)
    except Exception as err:
        print(err)
        return render(request,'index.html',{'posts':[], "current_user_id":id})

    return render(request,'index.html',{'posts':page, "current_user_id":id})


@login_required
def post_single(request, post):
 
    id=get_current_user_id(request)
    
    post=get_object_or_404(Post,slug=post,status='published')
    
    return render(request, 'single.html', {'post':post, "current_user_id":id})


@login_required
def author(request):

    id=get_current_user_id(request)
      
    all_users = User.objects.values()
  
    return render(request, 'authors.html', {'authors':all_users, "current_user_id":id})

@login_required
def blog(request,id):
    
    id=get_current_user_id(request)
    
    post=Post.objects.filter(author=id).order_by('-publish')

    return render(request, 'index.html', {'posts':post, "current_user_id":id})

def get_current_user_id(request):
    
    current_user = request.user

    id=current_user.id 

    return id
  