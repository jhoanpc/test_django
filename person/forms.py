from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    GENERE_CHOICES = [(Person.GenereType.FEMI,'Femenino'), (Person.GenereType.MALE,'Masculino')]
    TYPE_DOC = [(Person.TypeDoc.CC,"CC - Cédula de ciudadanía"), (Person.TypeDoc.NIT,'Nit')]
    
    class Meta:
        fields = fields = ('fullname', 'typedoc','nroDoc','gender')
        
        
    fullname = forms.CharField(label="Nombres Completos",
        widget=forms.TextInput(
        attrs={'placeholder': 'Luis Fernando Buitrago Almaestre',
               'class':'shadow appearance-none border rounded w-full py-4 px-6 rounded-xl'}
    ))    
    
    typedoc = forms.ChoiceField(choices=TYPE_DOC,label='Tipo de identificación',
        widget=forms.Select(
        attrs={'placeholder': 'Cedula',
               'class':'appearance-none w-full bg-white border hover:border-gray-500 px-6 py-4 pr-8 rounded-xl shadow leading-tight focus:outline-none focus:shadow-outline'}
    ),required=True)
    
    nroDoc = forms.CharField(min_length=6,max_length=20,label="Numero Identificación",
        widget=forms.TextInput(
        attrs={'placeholder': '335446289',
               'class':'shadow appearance-none border rounded w-full py-4 px-6 rounded-xl'}
    ))
    
    gender = forms.CharField(label="Genero",widget=forms.Select(choices=GENERE_CHOICES,
        attrs={'placeholder': 'Sexo',
               'class':'appearance-none w-full bg-white border hover:border-gray-500 px-5 py-4 pr-8 rounded-xl shadow leading-tight focus:outline-none focus:shadow-outline'}
    ))