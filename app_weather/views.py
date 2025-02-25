
from weather_api import current_weather

from django.http import JsonResponse


DIRECTION_TRANSFORM = {
    'n': 'северное',
    'nne': 'северо - северо - восточное',
    'ne': 'северо - восточное',
    'ene': 'восточно - северо - восточное',
    'e': 'восточное',
    'ese': 'восточно - юго - восточное',
    'se': 'юго - восточное',
    'sse': 'юго - юго - восточное',
    's': 'южное',
    'ssw': 'юго - юго - западное',
    'sw': 'юго - западное',
    'wsw': 'западно - юго - западное',
    'w': 'западное',
    'wnw': 'западно - северо - западное',
    'nw': 'северо - западное',
    'nnw': 'северо - северо - западное',
    'c': 'штиль',
}

def my_view(request):
    if request.method == "GET":
        data = current_weather(59.93, 30.31)
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})

if __name__ == "__main__":
    print(current_weather(59.93, 30.31))
