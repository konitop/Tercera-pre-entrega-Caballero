from django.shortcuts import render
from django.http import HttpResponse
from App.models import Viewer, Streamer, Video
from App.forms import ViewerFormulario, StreamerFormulario, VideoFormulario
# Create your views here.

def inicio(request):
    return render(request, "App/inicio.html")
def videos(request):
    return render(request, "App/videos.html")
def registro(request):
     return render(request, "App/Registro.html")
def streamers(request):
     return render(request, "App/Streamers.html")


def viewerFormulario(request):
      if request.method == "POST":
            miFormulario = ViewerFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  viewer = Viewer(
                       id=int(informacion['id']),
                       realname=str(informacion['Nombre']),
                       surname=str(informacion['Apellido']),
                       mail=informacion['mail']
                  )
                  viewer.save()
                  return render(request, "App/inicio.html")
      else:
            miFormulario = ViewerFormulario()
 
      return render(request, "App/viewerFormulario.html", {"miFormulario": miFormulario})


def streamerFormulario(request):
      if request.method == "POST":
            miFormulario = StreamerFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  streamer = Streamer(
                       id=int(informacion['id']),
                       username=str(informacion['username']),
                       realname=str(informacion['realname']),
                       surname=str(informacion['surname']),
                       mail=informacion['mail'],
                       link=str(informacion['link']),
                       img=str(informacion['img']),
                  )
                  streamer.save()
                  return render(request, "App/inicio.html")
      else:
            miFormulario = StreamerFormulario()
 
      return render(request, "App/streamerFormulario.html", {"miFormulario": miFormulario})


def videoFormulario(request):
      if request.method == "POST":
            miFormulario = VideoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  video = Video(
                       id= int(informacion['id']),
                       title= str(informacion['title']),
                       mins= int(informacion['mins']),
                       sec= int(informacion['sec']),
                       day= int(informacion['day']),
                       month= int(informacion['month']),
                       year= int(informacion['year']),
                       author= str(informacion['author']),
                       views= str(informacion['views']),
                       link= str(informacion['link']),
                       gif= str(informacion['gif']),
                       )
                  
                  video.save()
                  return render(request, "App/inicio.html")
      else:
            miFormulario = VideoFormulario()
 
      return render(request, "App/videoFormulario.html", {"miFormulario": miFormulario})



def busquedaVideo(request):
     return render(request,'App/busquedaVideo.html')

def buscarVideo(request):
     respuesta= f"Estoy buscando el video de: {request.GET['video']}"
     return HttpResponse(respuesta)


