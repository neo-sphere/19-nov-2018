from django.shortcuts import render

from django.http import HttpResponse

# function based  views
# def home(request):
    # return HttpResponse('Hello, World! Home Page!')

def home(request):
    context = {
        'title':'Home page jpt',
        'name':'Santosh Purbey'
    }
    return render(request, 'home.html', context)

def contact(request):
    return HttpResponse('Contact page !')
