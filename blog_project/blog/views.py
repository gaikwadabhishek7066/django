from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import PostForm, CommentForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    
    else:
        form = CommentForm()
    
    return render(request, 'blog/post_detail.html', {'post':post, 'comments':comments, 'form':form})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.Post)
        if form.is_valid():
            post = form.save(commit=True)
            post.author = request.User
            post.save()
            return redirect('post_list')
        
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
        
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form':form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')