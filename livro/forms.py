from django import forms
from .models import Livros

class CadastroLivros(forms.ModelForm):
    class Meta:
        model=Livros
        fields = ('__all__')
    def __init__ (self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()