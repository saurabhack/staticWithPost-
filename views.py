from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    
    return render(request,'index.html')

def profile(request):
    text2=request.GET['text2']

    return render(request,'profile.html' ,{'text2':text2})


