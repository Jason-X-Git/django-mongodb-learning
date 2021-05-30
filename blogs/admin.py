from django.contrib import admin

from .models import Entry, Blog, Article

admin.site.register(Entry)
admin.site.register(Article)