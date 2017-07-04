from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse


class IndexView(ListView):
    template_name = 'my_site/index.html'
    queryset = {}

