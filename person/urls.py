from .views import PersonView
from django.urls import path
urlpatterns = [
    path('', PersonView.index, name='people' )    
]