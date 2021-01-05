from django.shortcuts import render, redirect
from .models import Articles, Category, Tags

# Create your views here.

def category(request):
    categories = Category.objects.all
    tags = Tags.objects.all
    articles = Articles.objects.all
    context = {
        'categories': categories,
        'tags': tags,
        'articles': articles
    }
    return render(request, 'main/index.html', context)