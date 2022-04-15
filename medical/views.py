from django.template import loader
from django.http import HttpResponse
from rest_framework.throttling import AnonRateThrottle
from rest_framework.decorators import throttle_classes, api_view

from .models import Medicine
from .helpers import get_key_values_similarity

@api_view(['GET'])
@throttle_classes([AnonRateThrottle])
def index(request):
    keys = Medicine.objects.all().values('key')
    template = loader.get_template('home.html')
    context = {
        'keys': keys,
    }
    return HttpResponse(template.render(context, request))

@api_view(['GET'])
@throttle_classes([AnonRateThrottle])
def result(request):
    key = request.GET.get('keys')
    result = get_key_values_similarity(key=key)
    context = {
        'key': key,
        'result': result,
    }
    template = loader.get_template('result.html')
    return HttpResponse(template.render(context, request))
