from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    Post.objects.filter(published_date__lte=timezone.new()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

