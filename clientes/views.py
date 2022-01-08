from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def entrar(request):
    return render(request, 'auth-normal-sign-in.html')