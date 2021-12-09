from django.contrib.sitemaps import Sitemap 

from .models import Post 

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.publish.all()

    def lastmod(self, obj):
        return obj.published

    def location(self, obj):
        return obj.get_absolute_url()


        