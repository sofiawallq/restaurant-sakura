from django.shortcuts import render

def menues_view(request):
    return render(request, 'menues/menues.html')    