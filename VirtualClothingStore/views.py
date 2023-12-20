# Django
from django.http import HttpResponse

#Utilities
from datetime import datetime

def helloWorld(request):
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now = datetime.now().strftime('%b - %dth, %Y %H:%M hrs')
        ))
def hi(request):
    #import pdb; pdb.set_trace() 
    """
    PDB Se utiliza en Python para insertar un punto de interrupción en un programa, 
    lo que permite la depuración interactiva.
    Dentro del depurador, puedes usar comandos como n (siguiente), c (continuar), p (imprimir).
    Según la documentación puedes usar request.method, request.GET, etc
    """
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers))