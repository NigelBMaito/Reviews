from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

def posts_lists(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()


  
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  
            comment.save()
            return redirect('posts:page', slug=post.slug)
    else:
        form = CommentForm()  

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'posts/post_page.html', context)
