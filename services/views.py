from django.shortcuts import render
from core.models import SliderTop, Work, PeopleSay, PriceSection

# Create your views here.
def services(request):
    slider = SliderTop.objects.all()
    work = Work.objects.all()
    say = PeopleSay.objects.all()
    price = PriceSection.objects.all()

    context = {
        'slider': slider,
        'work': work,
        'say': say,
        'price': price,
    }

    return render(request, 'services/services.html', context)