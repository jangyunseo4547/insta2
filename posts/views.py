from django.shortcuts import render,redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    posts = Post.objects.all()
    form = CommentForm()

    context = {
        'posts':posts,
        'form':form,
    }
    return render(request,'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    
    context = {
        'form':form,
    }
    return render(request, 'create.html', context)

@login_required
def comment_create(request, post_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()

        return redirect('posts:index')

@login_required
def like(request, post_id):
    user = request.user     # 1) 어떤 유저가 어떤 게시글에 좋아요를 누를지
    post = Post.objects.get(id=post_id)

# 1) 유저 관점
    # if user in post.like_users.all(): #유저가 좋아요를 누른 유저에 있다면
    #     post.like_users.remove(user)      # 지우기
    # else:
    #     post.like_users.add(user)

    # return redirect('posts:index')

# 2) 게시글 관점
    if post in user.like_posts.all():
        user.like_posts.remove(post)
    else:
        user.like_posts.add(post)
    return redirect('posts:index')



