from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'director', 'is_active', 'created', 'updated')
    list_filter = ('is_active', 'director')
    search_fields = ('name', 'director')
    ordering = ('-created',)
    fields = ('name', 'duration', 'director', 'is_active', 'image')
    readonly_fields = ('created', 'updated')

admin.site.register(Movie, MovieAdmin)
