from django.shortcuts import render
from core.models import SliderTop
from .models import Blog

# Create your views here.
def blog(request):
    slider = SliderTop.objects.all()
    blog = Blog.objects.all()


    context = {
        'slider': slider,
        'blog': blog,
    }
    
    return render(request, 'blog/blog.html', context)
