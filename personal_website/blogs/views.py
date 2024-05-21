from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views import View
from .forms import CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect

class StartingPageView(ListView):
    template_name = 'blog/starting_page.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-date']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    context_object_name = 'all_posts'
    ordering = ['-date']


class SinglePostView(View):
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        is_saved_for_later = post.id in request.session.get('stored_post', [])
        # print(post.id, request.session.get('stored_post', []))
        # print(is_saved_for_later)
        return render(request,'blog/post-detail.html' , 
                      {'post': post, 
                       "comments": post.comments.all().order_by("-id"), # new
                       'comment_form': CommentForm(),
                    "is_saved_for_later": is_saved_for_later
                       
                       })  

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        is_saved_for_later = str(post.id) in request.session.get('stored_post', [])
        print(is_saved_for_later)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))

        return render(request,'blog/post-detail.html' ,context= {
            'post': post,
            "comments": post.comments.all().order_by("-id"),
            'comment_form': comment_form,
            "is_saved_for_later": is_saved_for_later,
        })
    
class ReadLaterView(View):
    def get(self,request):
        stored_post = request.session.get('stored_post')
        context_dict = {}
        if stored_post is None or len(stored_post) == 0:
            context_dict['posts'] = []
            context_dict['has_posts'] = False

        else:
            context_dict["posts"] = Post.objects.filter(id__in=stored_post)
            context_dict['has_posts'] = True
        return render(request, 'blog/stored-posts.html', context_dict)
    
    def post(self, request):
        stored_post = request.session.get('stored_post')
        if stored_post is None:
            stored_post = []

        if int(request.POST['post_id']) not in stored_post:
            stored_post.append(int(request.POST['post_id']))
            # print(stored_post)
        else:
            stored_post.remove(int(request.POST['post_id']))
        
        request.session['stored_post'] = stored_post
        return HttpResponseRedirect("/")
    
# def starting_page(request):
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     return render(request, 'blog/starting_page.html',context= {
#         'posts': latest_posts,
#     })

# def posts(request):
#     return render(request, 'blog/all-posts.html',context= {
#         'all_posts': Post.objects.all().order_by('-date'),
#     })

# def post_detail(request, post_id):
    
#     matching_post = get_object_or_404(Post,slug=post_id)
#     print(matching_post)
#     return render(request, 'blog/post-detail.html',context={
#         'post': matching_post
#     })