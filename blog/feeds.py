from django.contrib.syndication.views import Feed 

from .models import Post , Comment 

class LatestPostFeed(Feed):

    title = "Blog post site news"
    link = "/sitenews/"
    description = "Latest Posts added to blog."

    def items(self):
        return Post.publish.order_by('-published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body 
        