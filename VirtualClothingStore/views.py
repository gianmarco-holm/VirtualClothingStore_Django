# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime
import json

def helloWorld(request):
    """
    Muestra un saludo simple junto con la hora del servidor.
    """
    now = datetime.now().strftime('%b - %dth, %Y %H:%M hrs')
    response_data = {'message': 'Oh, hi! Current server time is {now}'.format(now=now)}
    return HttpResponse(response_data)

def sorted(request):
    """
    PDB se utiliza en Python para insertar un punto de interrupción en un programa,
    lo que permite la depuración interactiva.
    Dentro del depurador, puedes usar comandos como n (siguiente), c (continuar), p (imprimir).
    Según la documentación, puedes usar request.method, request.GET, etc.
    """
    numbers = sorted([int(x) for x in request.GET['numbers'].split(',')])
    data = {
        'status': 'ok',
        'data': numbers,
        'message': {
            'method': request.method,
            'path': request.path,
            'GET_parameters': request.GET.dict(),
            # Otros campos que desees incluir
        }
    }
    #return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
    return JsonResponse(data)

def sayHi(request, name, age):
    if age < 18:
        message = 'Sorry {}, no puedes pasar'.format(name)
    else:
        message = 'Hola {}, bienvenida al proyecto'.format(name)
    return HttpResponse(f'<h1><center>{message}</center></h1>')