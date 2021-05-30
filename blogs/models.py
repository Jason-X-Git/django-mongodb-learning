from django.db import models
from uuid import uuid1

from djongo import models

class Blog(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
    
    def __str__(self) -> str:
        return f'Blog {self.name}'
        
class Entry(models.Model):
    blog = models.EmbeddedField(
        model_container=Blog
    )
    
    headline = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'Entry {self.headline} - {self.blog}- {self.created}'
    
    
class Article(models.Model):
    id = models.UUIDField(default=uuid1, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'Article {self.name}'
    
    