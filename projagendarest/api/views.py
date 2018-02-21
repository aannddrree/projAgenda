from django.shortcuts import render
from rest_framework import generics
from .serializers import AgendaSerializer
from .models import Agenda

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
