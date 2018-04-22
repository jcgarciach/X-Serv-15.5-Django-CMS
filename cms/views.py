from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from .models import Pages

def barra(request):

    lista = Pages.objects.all()
    respuesta = "<ul>"
    for pag in lista:
        respuesta += '<li><a href = "/pages/' + str(pag.id) + '">' + pag.name + ">/a"
    respuesta += "</ul>"
    
    return HttpResponse (respuesta)

@csrf_exempt
     
def pages(request, num):
    if request.method == "POST":
        page = Pages(name = request.POST['name'], page = request.POST['page'])
        page.save()
        
    try:
        page = Pages.objects.get(id = str(num))
    except Pages.DoesNotExist:
        return HttpResponseNotFound ('<h1>' + num + 'Not Found </h1>')
    return HttpResponse(page.name + " " + str(page.page))
