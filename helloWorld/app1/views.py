from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):

    return render(request, 'page1.html',{'place':'Click2Cloud','chkProfile':'http://127.0.0.1:8000/profile'})

    #return HttpResponse("Hello World.!")


def profile(request):

    #return HttpResponse("Profile Page")
    return render(request, 'page2.html', {'nav': 'http://127.0.0.1:8000/','UT':'https://www.youtube.com/'})

def calculate(request):

    n1 = request.GET['num1']
    n2 = request.GET['num1']

    n3= int(n1)+int(n2)


    return render(request, 'calci.html',{'output':n3})