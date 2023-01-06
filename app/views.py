from django.shortcuts import render

# Create your views here.

def bcdn(request):
    return render(request,'bcdn.html')


def bd(request):
    return render(request,'bd.html')