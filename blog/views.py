from blog.forms import CommentForm, PostForm
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Comment, Post

from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form':form})
# 
@login_required
def post_new(request):

    if request.method == 'POST':
        # pegar formulario via requisição POST
        form = PostForm(request.POST)
        if form.is_valid():
            # salvar o formulario em variavel (commit=false) impede que salve direto no bd
            post = form.save(commit=False)
            # adicionar o autor
            post.author = request.user
            # adicionar data de publicação
            # post.published_date = timezone.now()
            # salvando no banco de dados
            post.save()
            #redirecionando para a pagina do post criado
            return redirect('post_detail', id=post.id)

    else:
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})


@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
        
    
    return render(request, 'blog/post_new.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required
def post_publish(request, id):
    post = get_object_or_404(Post, id=id)
    if not post.published_date:
        post.publish()
    return redirect('post_detail', id=id)


@login_required
def post_remove(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post_list')


@login_required
def comment_approve(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.approve()

    return redirect('post_detail', id=comment.post.id)

@login_required
def comment_remove(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    
    return redirect('post_detail', id=comment.post.id)