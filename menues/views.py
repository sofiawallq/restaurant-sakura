from django.shortcuts import render

def menues_view(request):
    return render(request, 'menues/menues.html')

def food_menu_view(request):
    return render(request, 'menues/food_menu.html')