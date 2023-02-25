from django.shortcuts import render,redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimo
from .forms import CadastroLivros

# Create your views here.


def home(request):
    if request.session.get('usuario'):
      usuario = Usuario.objects.get(id = request.session['usuario'])
      livros = Livros.objects.filter(usuario = usuario)
      form = CadastroLivros()
      form.fields['usuario'].initial = request.session['usuario']
      form.fields['categoria'].queryset = Categoria.objects.filter(usuario= usuario)


      return render(request, 'home.html', {'livros' : livros, 'form' : form, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/auth/login/?status=2')

def ver_livros(request, id):
  if request.session.get('usuario'):
      livro = Livros.objects.get(id = id)
      if request.session.get('usuario') == livro.usuario.id:
           usuario = Usuario.objects.get(id = request.session['usuario'])
           categoria_livro = Categoria.objects.filter(usuario_id= request.session.get('usuario'))
           emprestimos = Emprestimo.objects.filter(livro = livro)
           form = CadastroLivros()
           form.fields['usuario'].initial = request.session['usuario']
           form.fields['categoria'].queryset = Categoria.objects.filter(usuario= usuario)




           return render(request, 'ver_livro.html', {'livro' : livro, 'categoria_livro' : categoria_livro,'emprestimos' : emprestimos,'usuario_logado': request.session.get('usuario'),'form' : form})
      else:
        return HttpResponse('Esse livro nao e seu')
  return redirect('/auth/login/?status=2')



def cadastrar_livro(request):
  if request.method == 'POST':
    form = CadastroLivros(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/livro/home')
    else:
      return HttpResponse('DADOS INVALIDOS')
