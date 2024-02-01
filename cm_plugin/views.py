from django.http import JsonResponse
from django.http import HttpResponseNotFound, HttpResponse
import json
from .healthcheck import check_services

def get_info(request):
    data = {
        'message': 'Hello, this is a simple Django API!',
        'author': 'Your Name',
        'version': '1.0',
    }
    return JsonResponse(data)

def healthcheck(request):
    if request.GET.get('all', False):
        result = check_services()
    else:
        result = {'status': 'alive'}

    return HttpResponse(content=json.dumps(result), status=200, content_type="application/json")