from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Anime



def index(request):
    context = {'anime': Anime.objects.order_by('-score')}
    return render(request, 'index2.html', context)
    #return HttpResponse("Hello, world. You're at the MyNetflix list index.")

# Create your views here.
