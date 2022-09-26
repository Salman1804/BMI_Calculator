#from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from bmi.forms import BmiCalculator
from bmi.models import User

# Create your views here.
def add_show(request):
    if request.method=="POST":
        fm=BmiCalculator(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['FullName']
            gm=fm.cleaned_data['Gender']
            Ww=fm.cleaned_data['height']
            hw=fm.cleaned_data['Weight']
            bw=fm.cleaned_data['BMI_Calculate']
            reg=User(FullName=nm,Gender=gm,Weight=Ww,height=hw,BMI_Calculate=bw)
            reg.save()
            fm=BmiCalculator()
    else:
        fm=BmiCalculator() 
    stud=User.objects.all() 
    return render(request,'bmi/Show.html', {'form':fm ,'stu':stud} ) 

def delete_data(request,id):
       if request.method=="POST":
           pi = User.objects.get(pk=id)
           pi.delete()
           return HttpResponseRedirect ('/bmi/')



def update_data(request,id):
    if request.method=="POST":
        x=User.objects.get(pk=id)
        fm=BmiCalculator(request.POST,instance=x)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=BmiCalculator(instance=pi)
    return render (request,'bmi/update.html',{'form':fm})        
