from django.shortcuts import render
from .models import Phone

def list(request):
    contacts = Phone.objects.all().order_by('name')
    return render(request, 'contacts/list.html', {'contacts': contacts})

def result(request):

    if 'data' in request.GET:
        name = request.GET['data']
        contacts = Phone.objects.filter(name__contains=name).order_by('name')
    else:
        contacts = Phone.objects.all().order_by('name')

    return render(request, 'contacts/result.html', {'data': name, 'contacts': contacts})
