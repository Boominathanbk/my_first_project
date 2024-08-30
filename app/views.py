from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')


def kannur(request):
    return render(request,'kannur.html')

def mission(request):
    return render(request,'mission.html')    

def curry(request):
    return render(request,'curry.html')

