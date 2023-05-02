from django.db import models

# Create your models here.

class Viewer(models.Model):
    realname= models.CharField(max_length=25)
    surname= models.CharField(max_length=20)
    mail= models.EmailField()
    def __str__(self):
        return f"Nombre: {self.realname} |Apellido: {self.surname} |Correo: {self.mail}"
    
class Streamer(models.Model):
    username= models.CharField(max_length=30)
    realname = models.CharField(max_length=30)
    surname= models.CharField(max_length=30)
    mail= models.EmailField()
    link= models.CharField(max_length=150)
    img= models.CharField(max_length=300)
    

    def __str__(self):
        return f"Usuario: {self.username} |Nombre: {self.realname} |Apellido: {self.surname} |Correo: {self.mail}"
    
class Video(models.Model):
    title= models.CharField(max_length=50)
    mins= models.IntegerField()
    sec= models.IntegerField()
    day= models.IntegerField()
    month= models.IntegerField()
    year= models.IntegerField()
    author= models.CharField(max_length=25)
    views= models.CharField(max_length=11)
    link= models.CharField(max_length=300)
    gif= models.CharField(max_length=300)

    def __str__(self):
        return f"Título: {self.title} |Duración: {self.mins}:{self.sec} |Fecha: {self.day}/{self.month}/{self.year} |Autor: {self.author}"


