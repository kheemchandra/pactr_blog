from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.core.mail import send_mail
from django.db.models import Count 

from .models import Post 
from .forms import ShareForm, CommentForm


def post_list(request, tag=None):
    posts = Post.publish.all()
    if tag:
        posts = posts.filter(tags__name__in=[tag])
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 
                  'blog/post/post_list.html',
                  {'posts': posts,
                   'page_obj': page_obj})


def post_detail(request, post_id, slug):
    post = get_object_or_404(Post, id=post_id, slug=slug)
    similar_posts = Post.publish.filter(tags__in=post.tags.all()).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same=Count('tags')).order_by('-same', '-published')[:3]
    
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post 
            new_form.save()
    
    form = CommentForm()
    
    return render(request, 
                  'blog/post/post_detail.html',
                  {'post': post,
                  'similar_posts': similar_posts,
                  'form': form})

class PostListView(ListView):
    model = Post 
    paginate_by = 3 
    template_name = 'blog/post/post_list.html'
    queryset = Post.publish.all()

def post_share(request, post_id):
    form = ShareForm()
    sent = False
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subject = f"{data['name']} suggests you to check {post.title}"
            url = request.build_absolute_uri(post.get_absolute_url())
            message = f"{data['comment']}\nThe link is {url}"
            send_mail(
                subject,
                message,
                data['from_email'],
                [data['to_email'],],
                fail_silently=False,
            )
            sent = True 
    
    return render(request, 
                  'blog/post/post_share.html',
                  {'sent': sent,
                   'form': form,
                   'post': post,
                   })

