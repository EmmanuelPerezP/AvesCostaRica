from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from aves.models import Ave
from django.urls import reverse


class AveListView(ListView):
    model = Ave


class AveDetailView(DetailView):
    model = Ave
