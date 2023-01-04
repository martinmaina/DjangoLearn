from django.shortcuts import render
# A request handler, not a view in the sense of front-end 
# Create your views here.

from django.http import HttpResponse

def say_hello(request):
    return render(request, 'hello.htm', {'name':'Martin'})
