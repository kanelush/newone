from django.db import models
from django.forms import ModelForm

# Create your models here.



        
class Categ(models.Model):
    title = models.CharField(max_length=155)
    slug = models.SlugField(max_length=150)
    id = models.IntegerField(primary_key=True)

 
    def __str__(self):
        return self.title


class Negocio(models.Model):
    
    name = models.CharField(max_length=150)
    
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    
    fk = models.ForeignKey(Categ, on_delete=models.CASCADE)
   
    

    def __str__(self):
        return self.name

    

    


class Contacto(models.Model):
    name = models.CharField(max_length=150)
    mail = models.EmailField(blank=True, max_length=254)
    subject = models.CharField(max_length=150)
    description = models.TextField()
    

    def __str__(self):
        return self.name
    
