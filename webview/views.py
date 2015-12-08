from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response


def index(request):
    context = {
        'heading': "OpenMailArchive",
    }
    return render(request, 'welcome.html', context)

