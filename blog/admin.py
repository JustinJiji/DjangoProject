from django.contrib import admin
from .models import Post

admin.site.site_header='Web Admin'

admin.site.register(Post)


