from django.shortcuts import render,redirect
from django.views import View
from account.models import Contact,Staff
from home.models import Students
from .forms import Studentform
from django.contrib import messages


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Enquiry(View):
    def get(self,request):
        customer=Contact.objects.all()
        return render(request,'enquiry.html',{'form':customer}) 

class StaffS(View):
    def get(self,request):
        customer=Staff.objects.all()
        return render(request,'staff.html',{'form':customer})

class Showstudent(View):
    def get(self,request):
        student=Students.objects.all()
        return render(request,'showstudent.html',{'form':student})

class Form(View):
    def get(self,request):
        std1=Studentform()
        return render(request,'forms.html',{'form':std1})
    def post(self,request):
        if request.method == "POST":
            std1=Studentform(request.POST)
            if std1.is_valid():
                std1.save()
                student=Students.objects.all()
                return render(request,'showstudent.html',{'form':student})
            else:
                print("Form not valid")
            return redirect("showstudent")

class Show(View):
    def get(self,request):
        student=Students.objects.all()
        return render(request,'showstudent.html',{'form':student})

class Profile(View):
    def get(self,request):
        print(12)
        if request.session['email'] is not None:
            customer=Staff.objects.filter(email=request.session['email'])
            return render(request,'profile.html',{'form':customer})

class Edit(View):
    def get(self,request):
        edit1=request.session['email']
        edit=Staff.objects.filter(email=edit1)
        return render(request,'edit.html',{'form':edit})
    def post(self,request):
        edit1=request.session['email']
        print(1)
        if request.method=='POST':
            print(2)
            if Staff.objects.filter(email=edit1).exists():
                print(3)
                if request.POST['password']:
                    Staff.objects.filter(email=edit1).update(password=request.POST['password'])
                if request.POST['name']:
                    Staff.objects.filter(email=edit1).update(name=request.POST['name'])
                if request.POST['email']:
                    if Staff.objects.filter(email=edit1).exists():
                        edit=Staff.objects.filter(email=edit1)
                        messages.error(request,"EMAIL ALREADY EXISTS")
                        return render(request,'edit.html',{'form':edit})
                    else:
                        Staff.objects.filter(email=edit1).update(email=request.POST['email'])
                        request.session['email']=request.POST['email']
                if request.POST['phno']:
                    Staff.objects.filter(email=edit1).update(phno=request.POST['phno'])
                customer=Staff.objects.filter(email=request.session['email'])
                return render(request,'profile.html',{'form':customer})


                    
                    
