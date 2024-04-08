from django import forms
from .models import usuario

class usuarios(forms.ModelForm):
    class Meta:
        model = usuario  # Define o modelo com o qual o formulário está associado
        fields = ['nome', 'data_nascimento', 'email', 'pais']  # Especifica quais campos do modelo devem ser incluídos no formulário
