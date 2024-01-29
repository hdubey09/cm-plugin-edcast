from django.http import JsonResponse

def get_info(request):
    data = {
        'message': 'Hello, this is a simple Django API!',
        'author': 'Your Name',
        'version': '1.0',
    }
    return JsonResponse(data)
