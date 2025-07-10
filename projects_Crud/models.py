from django.db import models


class Projects(models.Model):
    title=models.CharField('Titulo', max_length=200)
    description= models.TextField('Descripción')
    technology=models.CharField('Tecnología', max_length=100)
    createt_At=models.DateTimeField('Creado',auto_now_add=True)
