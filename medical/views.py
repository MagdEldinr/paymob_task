from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Medicine


def index(request):
    keys = Medicine.objects.all().values('key')
    template = loader.get_template('home.html')
    context = {
        'keys': keys,
    }
    return HttpResponse(template.render(context, request))
