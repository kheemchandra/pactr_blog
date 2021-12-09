from django import template 
from django.db.models import Count
from django.utils import safestring 
from django.utils.safestring import mark_safe 

import markdown 

from ..models import Post 

register = template.Library()

@register.simple_tag 
def num_posts():
    return Post.publish.count()


@register.inclusion_tag('blog/tag1.html')
def most_recent_posts(cnt = 5):
    recent_posts =  Post.publish.order_by('-published')[:cnt]
    return {'recent_posts': recent_posts}

@register.inclusion_tag('blog/tag2.html')
def most_commented_posts(cnt = 5):
    commented_posts = Post.publish.annotate(no_of_comments=Count('comments')).order_by('-no_of_comments')[:cnt]
    return {'commented_posts': commented_posts}

@register.filter(name='markdown')
def markdown_post(text):
    html_text  = markdown.markdown(text)
    return mark_safe(html_text)


@register.inclusion_tag('blog/form_snippet.html')
def form_snippet(form):
    return {'form': form}