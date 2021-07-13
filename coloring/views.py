from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def save_share(request):
    return render(request, 'coloring/save_share.html')

def help(request):
    return render(request, 'coloring/help.html')

def library(request):
    return render(request, 'coloring/library.html')
