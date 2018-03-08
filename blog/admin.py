from django.contrib import admin
# imports model to be registered
from blog.models import Post, Entry

# tell django manage model through admin site and add post on the admin site
admin.site.register(Post)
# add a way to add entries on admin site
admin.site.register(Entry)



# Register your models here.
