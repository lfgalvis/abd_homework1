from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, 'retos/puntoa.html')
    return render_to_response('puntof.html')