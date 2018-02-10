from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render
from aves.models import Ave
from django.urls import reverse


class AveListView(ListView):
    model = Ave
