from django.http import HttpResponse
from django.shortcuts import render
from .models import Advertisement
from .forms import AdvertisementForm

def index(request):
    advertisements = Advertisement.objects.all()
    context={'advertisement':advertisements}
    return render(request,'index.html',context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    form = AdvertisementForm()
    context = render(request, 'advertisement-post.html',context)
    return render(request,'advertisement-post.html')
