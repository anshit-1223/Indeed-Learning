from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    sdata=slider.objects.all().order_by('-id')[0:3]
    nbdata=newbatches.objects.all().order_by('-id')[0:4]
    instdata=instructor.objects.all().order_by('id')[0:3]
    mydict={'data1':sdata,'data2':nbdata,'data3':instdata,}
    return render(request,'firstapp/index.html',mydict)

def aboutus(request):
    return render(request,'firstapp/aboutus.html')
def contact(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('phone')
        d=request.POST.get('msg')
        contactus(name=a,email=b,phone=c,msg=d).save()
        return HttpResponse("<script>alert('Thanks for contacting with us..');location.href='/fapp/contact/'</script>")
        # print(name,phone,email,msg)
        
    return render(request,'firstapp/contact.html')
def feedback(request):
    return render(request,'firstapp/feedback.html')

def login(request):
    if(request.method=="POST"):
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        x=signup.objects.filter(passwd=passwd,email=email).count()
        if x==1:
            request.session['user']=email
            y=signup.objects.filter(email=email,passwd=passwd)
            request.session['userpict']=str(y[0].profile)
            request.session['username']=str(y[0].name)
            request.session['batchid']=str(y[0].batchid)
            return HttpResponse("<script> location.href='/sapp/index/' </script>")
        else:
            return HttpResponse("<script>alert('Username or Password is Incorrect!!!'); location.href='/fapp/login/' </script>")
    return render(request,'firstapp/login.html')

def flogin(request):
    if(request.method=="POST"):
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        x=fsignup.objects.filter(passwd=passwd,email=email).count()
        if x==1:
            request.session['user']=email
            y=fsignup.objects.filter(email=email,passwd=passwd)
            # request.session['userpict']=str(y[0].profile)
            request.session['username']=str(y[0].name)
            request.session['fid']=str(y[0].fid)
            return HttpResponse("<script> location.href='/tapp/flindex/' </script>")
        else:
            return HttpResponse("<script>alert('Username or Password is Incorrect!!!'); location.href='/fapp/flogin/' </script>")
    return render(request,'firstapp/flogin.html')

def registration(request):
    bdata=studentbatch.objects.all().order_by('-id')
    md={"bdata":bdata,}
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        college=request.POST.get('college')
        course=request.POST.get('course')
        picture=request.FILES['fu']
        pyear=request.POST.get('pyear')
        batchid=request.POST.get('batch')
        x=signup.objects.filter(email=email).count()
        if x==0:
            signup(name=name,email=email,mobile=mobile,passwd=passwd,college=college,course=course,pyear=pyear,profile=picture,status='Pending',batchid=batchid).save()
            return HttpResponse("<script> alert('Registered Successfully'); location.href='/fapp/login/'</script>")
        else:
            return HttpResponse("<script> alert('Already Registered'); location.href='/fapp/registration/'</script>")
        # print(name,email,mobile,passwd,college,course,picture,pyear)
    return render(request,'firstapp/registration.html',md)

def placements(request):
    clg=request.GET.get('college')
    year=request.GET.get('year')
    collegedata=college.objects.all().order_by('-id')
    sessiondata=session_year.objects.all()
    # pdata=placement.objects.all().order_by('-id')
    if clg is not None and year is not None:
        pdata=placement.objects.filter(college=clg,session=year)
    else:
        pdata=placement.objects.all()
    placedict={'cdata':collegedata,'sdata':sessiondata,'pdata':pdata,}
    return render(request,'firstapp/placements.html',placedict)

def mynewbatches(request):
    batchdata=newbatches.objects.all().order_by('-id')
    batchdict={'bdata':batchdata,}
    return render(request,'firstapp/mynewbatches.html',batchdict)

def facility(request):
    return render(request,'firstapp/facility.html')