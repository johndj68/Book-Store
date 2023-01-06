from django.shortcuts import render,redirect
from django.http import HttpResponse
from usuarios.models import Usuario

# Create your views here.


def home(request):
    if request.session.get('usuario'):
      usuario = Usuario.objects.get(id = request.session['usuario'])
      return HttpResponse(f'oi bb {usuario}')
    else:
        return redirect('/auth/login/?status=2')
