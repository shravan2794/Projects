from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from .models import Register,Student,Sign,Session
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, StudentSerializer,SignSerializer,SessionSerializer
from django.views.generic import TemplateView
from rest_framework import viewsets
from . import models
from . import serializers



"""
posts=[
    {
        'author':'CoreyMS'
        'title':'Blog Post 1'
        'content':'first post content'
        'date_posted':'August 27 2020'

    }
    {
        'author':'Shravan Parikh'
        'title':'Blog Post 2'
        'content':'second post content'
        'date_posted':'August 27 2022'

    }
    
]
"""

def home(request):
    return render(request,'myapp/home.html')
def blog(request):
    return render(request,'myapp/about.html')

def student_view(request):
    y=forms.Studentform
    if request.method=='POST':
        y=forms.Studentform(request.POST)
        if y.is_valid():
            try:
                y.save()
            except:
                print('error saving')
    else:
        y=forms.Studentform()
    return render(request,'myapp/studentx.html',{'formx':y})
                

def form_view(request):
    form=forms.Registerform
    if request.method=="POST":
        form=forms.Registerform(request.POST)
        if form.is_valid():
            
            try:
                form.save()
                return redirect('/show/')
                
            except:
                print('error saving')
    else:
        form=forms.Registerform()
    return render(request,'myapp/index.html',{'form':form})


def success(request):
    return render(request,'myapp/success.html')

def show(request):
    x=Register.objects.all()
    return render(request,'myapp/show.html',{'Register': x})

class RandomView(TemplateView):
    template_name='myapp/home.html'

class LoginList(APIView):
    def get(self,request):
        values=Register.objects.all()
        Serializer=RegisterSerializer(values,many=True)
        return Response(Serializer.data)
class Studentlist(APIView):
    def get(self,request):
        z=Student.objects.all()
        c=StudentSerializer(z,many=True)
        return Response(c.data)

class RegisterViewset(viewsets.ModelViewSet):
    queryset=models.Register.objects.all()
    serializer_class=serializers.RegisterSerializer

class SignViewset(viewsets.ModelViewSet):
    queryset=models.Sign.objects.all()
    serializer_class=serializers.SignSerializer

class SessionViewset(viewsets.ModelViewSet):
    queryset=models.Session.objects.all()
    serializer_class=serializers.SessionSerializer

class StudentViewset(viewsets.ModelViewSet):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer




            
            
        
    
    



# Create your views here.
