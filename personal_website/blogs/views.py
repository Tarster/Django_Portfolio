from django.shortcuts import render,get_object_or_404
from .models import Post

def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/starting_page.html',context= {
        'posts': latest_posts,
    })

def posts(request):
    return render(request, 'blog/all-posts.html',context= {
        'all_posts': Post.objects.all().order_by('-date'),
    })

def post_detail(request, post_id):
    
    matching_post = get_object_or_404(Post,slug=post_id)
    print(matching_post)
    return render(request, 'blog/post-detail.html',context={
        'post': matching_post
    })