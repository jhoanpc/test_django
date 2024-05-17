from django.db import models
from utils.model_abstracts import Model
# Create your models here.
class Person(Model):
    class TypeDoc(models.TextChoices):
        NIT = "Nit"
        CC  = "CC"
    
    class GenereType(models.TextChoices):
        MALE = "Masculino"
        FEMI = "Femenino"
    
    fullname    = models.CharField(max_length=100, null=False)
    created_at  = models.DateTimeField(auto_now=True)
    typedoc     = models.CharField(max_length=4, choices=TypeDoc.choices, null=False)
    nroDoc      = models.CharField(max_length=14,null=False )
    gender      = models.CharField(max_length=10, null=False, choices=GenereType.choices)
    
    class Meta:
        verbose_name_plural='people'
    
    def __str__(self):
        return self.fullName