from django.shortcuts import redirect, render

def cursos(request):
    return render(request, 'cursos/todos-cursos.html')