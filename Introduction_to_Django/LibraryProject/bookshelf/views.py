from django.shortcuts import render
from django.http import HTTPResponse



def say_hello(request):
    return HTTPResponse('Hello World')
 