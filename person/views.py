from django.shortcuts import render
from .forms import PersonForm

# Create your views here.


class PersonView():
    
    def index(request):
        form = PersonForm
        return render(request,'person/person.html',{
            'form':form
        })