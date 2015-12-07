from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('welcome.html')
    context = RequestContext(request, {
        'heading': "OpenMailArchive",
    })
    return HttpResponse(template.render(context))