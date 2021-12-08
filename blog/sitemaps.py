from django.contrib.sitemaps import Sitemap 

from .models import Post, Comment 

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.publish.all()

    def lastmod(self, obj):
        return obj.published

    def location(self, obj):
        return obj.get_absolute_url()


class CommentSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Comment.objects.all()

    def lastmod(self, obj):
        return obj.commented    

    def location(self, obj):
        return obj.post.get_absolute_url()