from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return render(request, 'landing_page/index.html')