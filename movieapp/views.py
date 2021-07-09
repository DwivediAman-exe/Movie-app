from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    movie_data = Movie.objects.all()
    return render(request, 'home.html', {"movie": movie_data})


def testimonials(request):
    return render(request, 'testimonials.html', {})


def movie(request, movie_id):
    movie_data = Movie.objects.get(id=movie_id)
    return render(request, 'movie.html', {"movie": movie_data})
