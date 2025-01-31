from django.urls import path
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

def count_characters(request, word):
    count = len(word)
    return JsonResponse({'word': word, 'count': count})

urlpatterns = [
    path('count_characters/<str:word>/', count_characters, name='count_characters'),
]
@csrf_exempt
@require_POST
def factorial(request):
    try:
        # Intentamos cargar el cuerpo de la solicitud como JSON
        data = json.loads(request.body)
        # Obtenemos el valor de 'number' y verificamos que sea un número entero
        number = data.get('number')

        # Comprobamos que el número sea válido: que sea un entero no negativo
        if number is None or not isinstance(number, int) or number < 0:
            return JsonResponse({'error': 'Invalid input'}, status=400)
        
        # Función recursiva para calcular el factorial
        def calculate_factorial(n):
            if n == 0:
                return 1
            else:
                return n * calculate_factorial(n-1)
        
        # Llamamos a la función para obtener el factorial
        result = calculate_factorial(number)
        
        # Retornamos la respuesta con el número y el factorial calculado
        return JsonResponse({'number': number, 'factorial': result})

    except json.JSONDecodeError:
        # Si el cuerpo no es un JSON válido, retornamos un error
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

urlpatterns += [
    path('factorial/', factorial, name='factorial'),
]