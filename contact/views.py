from django.shortcuts import render, redirect
from core.models import SliderTop
from .forms import CommentForm

# Create your views here.
def contact(request):
    slider = SliderTop.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = CommentForm()

    context = {
        'slider': slider,
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
