from django import forms

from .models import ket

class PostForm(forms.ModelForm):

    class Meta:
        model = ket
        fields = ('nombre', 'peso', 'estatura', 'edad', 'sexo')