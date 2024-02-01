from django.urls import path
from .views import *

urlpatterns = [
    path('api/info/', get_info, name='get_info'),
    path('cm/healthcheck/', healthcheck),
]
