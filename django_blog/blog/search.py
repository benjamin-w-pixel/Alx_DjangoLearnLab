from django.db.models import Q
from .models import Post

def search_posts(query):
    return Post.objects.filter(
        Q(title__icontains=query) | 
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()