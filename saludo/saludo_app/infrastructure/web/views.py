import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from saludo_app.application.services.saludar_service import SaludarService

@csrf_exempt
def saludar_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('name', '')
    else:
        nombre = request.GET.get('name', '')

    servicio = SaludarService()
    resultado = servicio.ejecutar(nombre)
    return HttpResponse(resultado)