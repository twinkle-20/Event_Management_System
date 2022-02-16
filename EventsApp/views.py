from itertools import count
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from flask_login import current_user
from .models import *
# Create your views here.

def home(request):
    return render(request,'events/home.html')

def userlogin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=uname,password=password)

        if user is not None:
            login(request,user)
            eve = AddEvents.objects.all()
            context = {'Events':eve}
            return render(request,'events/vieweventspage.html',context)
        else:
            msg = 'Invalid Credentials!!'
            return render(request,'events/userloginpage.html',{'msg':msg})

    return render(request,'events/userloginpage.html')

def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        uname = request.POST['username']
        passw = request.POST['pass'] 
        password = request.POST['password']

        if password!=passw:
            status = "Password does not match!!!"
            return render(request,"events/register.html",{'status':status})

        #checking if queryset is empty
        if User.objects.filter(username=uname).exists():
            status = "Username already exists!!!"
            return render(request,"events/register.html",{'status':status})

        User.objects.create_user(username=uname,password=password).save()
        lastobj = len(User.objects.all())-1
        StudRegData(id=User.objects.all()[int(lastobj)].id,Name=name,Username=User.objects.all()[int(lastobj)].username,Password=User.objects.all()[int(lastobj)].password).save()

        msgdisp = "Data Stored Successfully!!"
        return render(request,"events/userloginpage.html",{'msg':msgdisp})
    
    return render(request,"events/register.html")

def viewevents(request):
    eve = AddEvents.objects.all()
    context = {'Events':eve}
    return render(request,"events/vieweventspage.html",context)

def logoutall(request):
    logout(request)
    return render(request,"events/userloginpage.html")
    
#Getting user clicked event details in eventenroll.html
def eventenrollact(request,eveid):

    curruser=request.user.id
    details = AddEvents.objects.filter(pk=eveid)
    studata = StudRegData.objects.filter(pk=curruser)
    return render(request,"events/eventenroll.html",{'eventdetails':details,'studata':studata})

#Entering Final event registration details into database
def eventenrolled(request):
    if request.method=="POST":
    
        current_user = request.user.username

        ename = request.POST['evename']
        ecost = request.POST['evecost']
        edur = request.POST['evedur']
        estartdate = request.POST['evestartdate']
        sname = request.POST['studname']
        sphone = request.POST['phone']

        chkeve =  StudentEnrolledEvents.objects.filter(StudUsername=current_user,EName=ename).count()
 
        if chkeve>=1:
            msg = "You have already participated in this event!!!"
            context = {'msgeve':msg}
            return render(request,"events/vieweventspage.html",context)
        else:
            StudentEnrolledEvents(EName=ename,EDuration=edur,ECost=ecost,EStartDate=estartdate,StudName=sname,StudUsername=request.user.username,ContactNo=sphone).save()
            # Getting amount of the events for the Main payment page
            amt = StudentEnrolledEvents.objects.filter(StudUsername=current_user) & StudentEnrolledEvents.objects.filter(EName=ename)
            return render(request,"events/payment.html",{'amt':amt})

def studash(request):

    #displaying student details with the events he/she enrolled for
    current_user = request.user.username
    det = StudentEnrolledEvents.objects.filter(StudUsername=current_user)

    if det.exists():
        return render(request,"events/studash.html",{'details':det})
    else:
        msg = "You havent enrolled for any events!!!"
        context = {'msg':msg}
        return render(request,"events/studash.html",context)