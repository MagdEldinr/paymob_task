from django.template import loader
from django.http import HttpResponse
from ratelimit.decorators import ratelimit

from .models import Medicine
from .helpers import get_key_values_similarity


def index(request):
    keys = Medicine.objects.all().values('key')
    template = loader.get_template('home.html')
    context = {
        'keys': keys,
    }
    return HttpResponse(template.render(context, request))

def result(request):
    key = request.GET.get('keys')
    result = get_key_values_similarity(key=key)
    context = {
        'key': key,
        'result': result,
    }
    template = loader.get_template('result.html')
    return HttpResponse(template.render(context, request))
