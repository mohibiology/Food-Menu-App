from django.shortcuts import render
from .models import Moviedata
from .serializers import MovieSerializer
from rest_framework import viewsets

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer
    # Create your views here.