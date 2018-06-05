from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from aves.models import Ave, Image
from django.urls import reverse

from aves.serializers import AveSerializer
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
