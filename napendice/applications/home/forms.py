from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'telephone',
            'subject',
            'send',
        ]
        labels = {
            'name': 'nombre',
            'email': 'email',
            'telephone': 'telefono',
            'subject': 'asunto',
            'send': 'consulta',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'telephone':forms.TextInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'send':forms.Textarea(attrs={'class':'form-control'}),
        }


class SearchForm(forms.Form):
    '''
    formulario para buscar notas
    '''
    kword = forms.CharField(
        max_length='300',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Buscar'
            }
        )
    )
