from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hello(request):
  return HttpResponse('Hello Awesome World')

def home(request):
  return HttpResponse('This is the Index Page')

def current_datetime(request):
  current_date = datetime.datetime.now()
  return render_to_response('current_datetime.html',locals())

def hours_ahead(request, offset):
  try:
    hour_offset = int(offset)
  except ValueError():
    raise Http404()
  next_time = datetime.datetime.now() + datetime.timedelta(hours = hour_offset)
  return render_to_response('hours_ahead.html',locals())

def search_form(request):
  return render_to_response('search_form.html')