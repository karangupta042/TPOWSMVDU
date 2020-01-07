from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    posts=Post.objects
    return render(request,'posts/home.html',{'posts':posts})
@login_required
def detail(request,post_id):
    detailpost=get_object_or_404(Post,pk=post_id)
    return render(request,'posts/detail.html',{'detail':detailpost})