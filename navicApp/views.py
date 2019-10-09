from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from navicApp import dataServe


@csrf_exempt
def getData(request):
    if request.method == 'POST':
        data = dataServe.getdata()
        return render(request, 'index.html',{"r":data})
