from django.shortcuts import render, redirect, HttpResponseRedirect,HttpResponse
from .models import Member
from bmi.forms import BmiCalculator
from bmi.models import User
from django.core.mail import send_mail
# Create your views here.

def index(request):
    if request.method == 'POST':
        member = Member.objects.get(Email=request.POST['Email'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
        send_mail(
            'RAGISTRATION CONFORMATION',
            'Hello {{ member.firstname }} , thank you for ragistration.',
            'salmangolandaj32@gmail.com',
            ['{{ member.Email }}'] ,
            fail_silently= False
        )
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'bmi/show.html',)
        
    else:
            
        context = {'msg': 'Invalid username or password'}
        
    return render(request, 'login.html', context)


def home(request):
    if request.method == 'POST':
                
        fm=BmiCalculator(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['FullName']
            gm=fm.cleaned_data['Gender']
            Ww=fm.cleaned_data['height']
            hw=fm.cleaned_data['Weight']
            bw=fm.cleaned_data['BMI_Calculate']
            reg=User(FullName=nm,Gender=gm,Weight=Ww,height=hw,BMI_Calculate=bw)
            reg.save()
            send_mail(
            'Hello {{ member.firstname, your details are below}}',
            'Your fullname : {{ User.Fullname }} \n Gender is : {{ User.Gender }} \n Your Height is : {{ User.Weight }} \n Yoour BMI is : {{ User.BMI_Calculate }}',
            'salmangolandaj32@gmail.com',
            ['{{ member.Email }}'] ,
            fail_silently= False
            )
            fm=BmiCalculator()
        else:
            fm=BmiCalculator() 
        stud=User.objects.all() 
        return render (request,'bmi/show.html',{'form':fm ,'stu':stud } ) 
            
            


        