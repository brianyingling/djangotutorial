from django.http import HttpResponse

def hello(request):
  return HttpResponse('Hello World')

def search_form(request):
  return HttpResponse('got here')