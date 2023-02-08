from django.http import HttpResponse
from django.shortcuts import render
from . models import Travel
from . models import Teams
# Create your views here.
#def home(request):
 #return HttpResponse("Welcome to homepage")
#def about(request):
 ####def detail(request):
  # return HttpResponse("Hello User")
#def thanks(request):
#  return render(request,"thanks.html")
def demo(request):
    obj=Travel.objects.all()
    obje=Teams.objects.all()
    return render(request,"index.html",{'result':obj,'res':obje})
#virtualenv name:demo
def credentialsapp():
    return None