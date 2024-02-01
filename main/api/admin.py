from django.contrib import admin
from .models import Movie

class MoviesAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'genre']
admin.site.register(Movie, MoviesAdmin)


