from django.shortcuts import render
from core.models import SliderTop

from .models import SndWall

# Create your views here.
def features(request):
    slider = SliderTop.objects.all()
    slider2 = SndWall.objects.all()

    context = {
        'slider': slider,
        'slider2': slider2,
    }

    return render(request, 'features/features.html', context)
