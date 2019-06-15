from django.shortcuts import render
from .models import SliderTop, FstWall, Work, PeopleSay, PriceSection, Blog

# Create your views here.

def home(request):
    slider = SliderTop.objects.all()
    f_wall = FstWall.objects.order_by('-id').first()
    work = Work.objects.all()[:3]
    say = PeopleSay.objects.all()
    price = PriceSection.objects.all()
    blog = Blog.objects.all()

    context = {
        'slider': slider,
        'f_wall': f_wall,
        'work': work,
        'say': say,
        'price': price,
        'blog': blog,
    }
    return render(request, 'core/home.html', context)