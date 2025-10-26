from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm

def home(request):
    return render(request, 'movies/home.html')

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

def display_movie(request):
    movie = None
    if request.method == 'POST':
        name = request.POST.get('name')
        movie = Movie.objects.filter(name__iexact=name).first()
    return render(request, 'movies/display_movie.html', {'movie': movie})

def edit_movie(request):
    movie = None
    not_found = False
    if request.method == 'POST' and 'search' in request.POST:
        name = request.POST.get('name')
        movie = Movie.objects.filter(name__iexact=name).first()
        if not movie:
            not_found = True
    elif request.method == 'POST' and 'update' in request.POST:
        movie = get_object_or_404(Movie, id=request.POST.get('movie_id'))
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'movies/edit_movie.html', {'form': form, 'movie': movie})
    if movie:
        form = MovieForm(instance=movie)
        return render(request, 'movies/edit_movie.html', {'form': form, 'movie': movie})
    return render(request, 'movies/edit_movie.html', {'not_found': not_found})

def delete_movie(request):
    deleted = False
    if request.method == 'POST':
        name = request.POST.get('name')
        movie = Movie.objects.filter(name__iexact=name).first()
        if movie:
            movie.delete()
            deleted = True
    return render(request, 'movies/delete_movie.html', {'deleted': deleted})