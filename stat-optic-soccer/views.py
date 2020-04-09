import os
import subprocess
from django.shortcuts import render
from .scope import Scope

from django.http import HttpResponse


def index(request):
    whom = os.getenv('POWERED_BY', 'Deis')
    release = os.getenv('WORKFLOW_RELEASE', 'unknown')
    container = subprocess.getoutput('hostname').strip()
    return HttpResponse('Welcome to stat-optic-soccer!'.format(**locals()))


# Return 200 for kubernetes healthcheck.
def healthz(request):
    return HttpResponse('')


def soccer_index(request):
    return render(request, 'soccer_index.html')#, context=scope.context)
