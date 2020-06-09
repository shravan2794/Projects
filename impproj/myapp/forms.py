from django import forms
from django.core import validators
from django.forms import ModelForm
from .models import Register,Student



#def check(value):
   # if value[0].lower() != 'a':
       # raise forms.ValidationError('Please enter name starting with a')
#def valid(password):
   # count=0
   # count1=0
   # count2=0
   # count3=0
    #for x in password:
      #  if x.isupper():
         #   count=count+1
       # if x.islower():
         #   count1=count1+1
       # if x in ('[@_!#$%^&*()<>?/\|}{~:]'):
        #if x in ('1234567890'):
          ## if count <1 or count1<1 or count2<1 or count3<1:
       # raise forms.ValidationError('Please enter atleast one of each')


#def check1(email):
  #   if email==Registerform.email():
       #  pass
    # else:
     #    raise forms.ValidationError('Please both email should match')
        
        





        


    
    

class Registerform(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"

class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        
    

 


