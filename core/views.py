from django.shortcuts import render

def splash(request):
    return render(request, 'splash.html', {})

def apply(request):
    return render(request, 'apply.html', {})

def read(request):
    return render(request, 'read.html', {})