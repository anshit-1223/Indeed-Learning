from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from firstapp.models import *

# Create your views here.
def index(request):
    return render(request,'secondapp/index.html')

def batches(request):
    batchdata=newbatches.objects.all().order_by('-id')
    batchdict={'bdata':batchdata,}
    return render(request,'secondapp/batches.html',batchdict)

def lectures(request):
    cdata=category.objects.all().order_by('-id')
    cd={"cdata":cdata,}
    return render(request,'secondapp/lectures.html',cd)

def liveclasses(request):
    batchid=request.session.get('batchid')
    data=batchtiming.objects.filter(batch=batchid)
    md={'data':data,}
    return render(request,'secondapp/liveclasses.html',md)

def logout(request):
    user=request.session.get('user')
    if user:
        del request.session['user']
        del request.session['userpict']
        del request.session['username']
        return HttpResponse("<script>location.href='/fapp/login/'</script>")
    return render(request,'secondapp/logout.html')

def note(request):
    bid=request.session.get('batchid')
    ndata=enotes.objects.filter(batch=bid)
    md={"ndata":ndata,}
    return render(request,'secondapp/note.html',md)

def softwarekit(request):
    x=mysoftware.objects.all().order_by('-id')
    md={'sdata':x,}
    return render(request,'secondapp/softwarekit.html',md)

def tasks(request):
    user=request.session.get('user')
    batchid=request.session.get('batchid')
    tdata=""
    if user:
        tdata=mytask.objects.filter(taskbatch=batchid)
        mdata=submittedtask.objects.filter(userid=user)
        md={'tdata':tdata,'mdata':mdata,}
    return render(request,'secondapp/tasks.html',md)

def uprofile(request):
    user=request.session.get('user')
    udata=signup.objects.filter(email=user)
    batchid=str(udata[0].batchid)
    status=str(udata[0].status)
    md={'udata':udata,}
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        college=request.POST.get('college')
        course=request.POST.get('course')
        picture=request.FILES['fu']
        pyear=request.POST.get('pyear')
        signup(name=name,mobile=mobile,college=college,course=course,profile=picture,passwd=passwd,pyear=pyear,email=user,batchid=batchid,status=status).save()
        return HttpResponse("<script>alert('Profile Updated Successfully...'); location.href='/sapp/uprofile'</script>")
    return render(request,'secondapp/uprofile.html',md)

def lecturesvideo(request):
    batchid=request.session.get('batchid')
    cid=request.GET.get('cid')
    lvdata=mylectures.objects.filter(video_category=cid,video_batch=batchid)
    md={'lvdata':lvdata,}
    return render(request,'secondapp/lecturesvideo.html',md)

def stask(request):
    user=request.session.get('user')
    if request.method=="POST":
        tid=request.POST.get('tid')
        title=request.POST.get('title')
        answer_file=request.FILES['fu']
        x=submittedtask.objects.filter(tid=tid,userid=user).count()
        if x==1:
            return HttpResponse("<script>alert('Task Already Submitted...');location.href='/sapp/tasks';</script>")
        else:
            submittedtask(title=title,answer_file=answer_file,userid=user,tid=tid).save()
            return HttpResponse("<script>alert('Task Submitted...');location.href='/sapp/tasks';</script>")
    return render(request,'secondapp/stask.html')
