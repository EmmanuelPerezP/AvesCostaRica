from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from aves.models import Ave, Image, Clase, Orden, Familia, Genero, Especie
from django.urls import reverse

from aves.serializers import AveSerializer, ClaseSerializer, OrdenSerializer, FamiliaSerializer, GeneroSerializer, EspecieSerializer
from rest_framework import generics


class AveListView(ListView):
    model = Ave


class AveDetailView(DetailView):
    model = Ave

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imagenes'] = Image.objects.filter(Ave=self.object.id)
        return context


class AvesList(generics.ListAPIView):
    # como hacer un where para el orm de django
    # https://docs.djangoproject.com/en/2.0/ref/models/querysets/#gt
    # https://docs.djangoproject.com/en/2.0/topics/db/queries/#field-lookups
    queryset = Ave.objects.all()
    serializer_class = AveSerializer


class ClaseList(generics.ListAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer


class OrdenList(generics.ListAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer


class FamiliaList(generics.ListAPIView):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer


class GeneroList(generics.ListAPIView):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class EspecieList(generics.ListAPIView):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer
