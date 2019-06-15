from django.shortcuts import render
from core.models import SliderTop, Work, PeopleSay

# Create your views here.
def about(request):
    slider = SliderTop.objects.all()
    work = Work.objects.all()[:3]
    say = PeopleSay.objects.all()

    context = {
        'slider': slider,
        'work': work,
        'say': say,
    }

    return render(request, 'about/about.html', context)