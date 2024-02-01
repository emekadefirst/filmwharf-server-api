from django.urls import path
from .views import MovieView, SearchMovieView, PageView

urlpatterns = [
    path('', PageView.as_view(), name='page'),
    path('api', MovieView.as_view(), name='home'),
    path('search', SearchMovieView.as_view(), name='search'),
]
