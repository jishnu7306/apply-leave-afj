from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

#common al se ji

def Applyleave(request):
    return render(request, 'Applyleave.html')
    
#jishnu 

def applyleavesub(request):
    return render(request, 'applyleavesub.html')

#sebin

def Requestedleave(request):
    return render(request, 'Requestedleave.html')

#althaf

def trainers_leave(request):
    return render(request, 'trainers_leave.html')
def trainees_leave(request):
    return render(request, 'trainees_leave.html')

