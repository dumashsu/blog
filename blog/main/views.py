from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    return HttpResponse('Hello world!')