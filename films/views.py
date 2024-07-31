from django.shortcuts import render, redirect
from .models import Movie
from films.constans import PAGE_SIZE

from .forms import MovieForm
from django.http import HttpResponseNotFound


def main_page_view(request):
    search_query = request.GET.get('search', '')
    page_number = int(request.GET.get('page', 1))

    movies = Movie.objects.filter(is_active=True)
    if search_query:
        movies = movies.filter(name__icontains=search_query) | movies.filter(director__icontains=search_query)
    
    total_movies = movies.count()
    start_index = (page_number - 1) * PAGE_SIZE
    end_index = start_index + PAGE_SIZE
    movies_page = movies[start_index:end_index]

    total_pages = (total_movies + PAGE_SIZE - 1) // PAGE_SIZE 
    context = {
        'movie_list': movies_page,
        'search_query': search_query,
        'total_pages': total_pages,
        'current_page': page_number,
    }
    return render(request, 'movie_list.html', context)

def movie_detail_view(request, id):
    movie = Movie.objects.filter(id=id).first()

    if movie is None:
        return render(request, '404.html', status=404)

    return render(request, 'movie_detail.html', {'movie': movie})

def movie_create_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form})

def movie_update_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return HttpResponseNotFound("Movie not found")

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', id=movie.id)
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'movie_form.html', {'form': form})

def movie_delete_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return HttpResponseNotFound("Movie not found")

    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    
    return render(request, 'movie_confirm_delete.html', {'movie': movie})

