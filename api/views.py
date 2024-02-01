from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.http import HttpRequest
from .models import Movie
from django.db.models.functions import Lower


from django.db.models import Q
from rest_framework import status
from django.http import HttpResponse

class PageView(APIView):
    def get(self, request, *args, **kwargs):
        message = "Endpoints: /api, search"
        return Response(message, status=status.HTTP_200_OK)

class MovieView(APIView):
    def get(self, request):
        query = Movie.objects.all()
        serializer = MovieSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchMovieView(APIView):
    def post(self, request):
        search_query = request.data.get('query', '')
        print(f"Received search query: {search_query}")

        if search_query is not None:
            search_results = Movie.objects.filter(
                Q(name__icontains=search_query) |
                Q(genre__icontains=search_query) | 
                Q(download_link__icontains=search_query) |
                Q(source__icontains=search_query) |
                Q(thumbnail_url__icontains=search_query) |
                Q(release_date__icontains=search_query)  
            )

            search_results = search_results.order_by(Lower('name'))

            serializer = MovieSerializer(search_results, many=True)
            return Response(serializer.data)
        else:
            return Response("Invalid search query", status=status.HTTP_400_BAD_REQUEST)



