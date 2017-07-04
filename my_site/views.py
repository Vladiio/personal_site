from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse


class IndexView(ListView):
    pass


def index_view(request):
    return HttpResponse('Hello word')
