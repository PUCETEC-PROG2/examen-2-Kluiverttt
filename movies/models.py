from django.db import models

# Create your models here.
class Movies (models.Model):
    id =  models.IntegerField(null=False)
    titulo = models.CharField(max_length=30, null=False)
    genero  = models.CharField(max_length=30, null=False)
    director = models.CharField(max_length=30, null=False)
    añopublicacion = models.IntegerField(null=False)
    sinopsis = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.titulo
    from django.db import models


