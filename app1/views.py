from django.http import HttpResponse
from django.shortcuts import render
from app1.models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request):
    posts = Post.objects.all()
    post = posts.order_by('id')[1]
    return render(
        request,
        'app1/index.html',
        {'posts':posts,}
        )

@login_required
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'app1/new.html', {'form':form})
