from django.contrib import admin
from .models import Livros,Categoria,Emprestimo


admin.site.register(Categoria)
admin.site.register(Livros)
admin.site.register(Emprestimo)