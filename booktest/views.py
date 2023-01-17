from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from .models import *


# Create your views here.

def index(request):
    # temp = loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    context = {'title': '123'}

    booklist = BookInfo.objects.all()
    context = {'list': booklist}

    return render(request, 'booktest/index.html', context)
