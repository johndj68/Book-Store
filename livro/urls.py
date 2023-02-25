from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('ver_livro/<int:id>', views.ver_livros, name='ver_livros'),
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),
]
