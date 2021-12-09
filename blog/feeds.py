from django.contrib.syndication.views import Feed 
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy

from .models import Post 

class LatestPostFeed(Feed):

    title = "Blog post site news"
    link = reverse_lazy('blog:post_list')
    description = "Latest Posts added to blog."

    def items(self):
        return Post.publish.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30) 
        