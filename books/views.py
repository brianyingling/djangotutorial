from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book

def search_form(request):
  return render_to_response('search_form.html')

def search(request):
  errors = []
  if 'q' in request.GET:
    q = request.GET['q']
    if not q:
      errors.append('Please enter a search term.')
    elif len(q) > 20:
      errors.append('Query must be 20 characters or less.')
    else:
      books = Book.objects.filter(title__icontains=q)
      return render_to_response('search_results.html', {'books':books,'query':q})
    # return render_to_response('search_results.html')
  else:
    return render_to_response('search_form.html', {'error':True} )

