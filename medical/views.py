from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework.throttling import AnonRateThrottle
from rest_framework.decorators import throttle_classes, api_view

from .utilities.helpers import get_key_values_similarity, load_column_from_dataset

@api_view(['GET'])
@throttle_classes([AnonRateThrottle])
def index(request):
    keys = load_column_from_dataset('Key')
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

def throtlling(request, exception):
    return render(request, 'errors/429.html')

def server_error(request):
    return render(request, 'errors/429.html')