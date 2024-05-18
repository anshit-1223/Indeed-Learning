from django.http import HttpResponse
from django.shortcuts import render
from firstapp.models import *


# Create your views here.
def findex(request):
    return render(request,'thirdapp/findex.html')

def flogout(request):
    user=request.session.get('user')
    if user:
        del request.session['user']
        # del request.session['userpict']
        del request.session['username']
        return HttpResponse("<script>location.href='/fapp/flogin/'</script>")
    return render(request,'thirdapp/flogout.html')

def fenotes(request):
    bdata=studentbatch.objects.all().order_by('-id')
    notes=enotes.objects.all().order_by('-id')
    if request.method=='POST':
        notename=request.POST.get('notename')
        notepic=request.POST.get('notepic')
        notefile=request.POST.get('notefile')
        addeddate=request.POST.get('addeddate')
        batch=request.POST.get('batch')
        batch_name=studentbatch.objects.get(id=batch)
        batch=enotes()
        batch.enotes=batch_name
        enotes(title=notename,notes_pic=notepic,pdf_notes=notefile,added_date=addeddate,batch=batch_name).save()
    md={"bdata":bdata,'edata':notes}
    return render(request,'thirdapp/fenotes.html',md)

def fonclass(request):
    data=batchtiming.objects.filter()
    bdata=studentbatch.objects.all().order_by('-id')
    md={'data':data,"bdata":bdata,}
    if request.method=='POST':
        name=request.POST.get('title')
        time=request.POST.get('time')
        link=request.POST.get('clink')
        cldate=request.POST.get('cdate')
        batch=request.POST.get('batch')
        batch_name=studentbatch.objects.get(id=batch)
        batch=batchtiming()
        batch.batchtiming=batch_name
        batchtiming(clname=name,batch=batch_name,clink=link,timing=time,start_date=cldate).save()
    return render(request,'thirdapp/fonclass.html',md)

def fetask(request):
    td=mytask.objects.all().order_by('-id')
    bdata=studentbatch.objects.all().order_by('-id')
    md={'tdata':td,'bdata':bdata}
    if request.method=='POST':
        task=request.POST.get('task')
        cfile=request.POST.get('cfile')
        cdate=request.POST.get('cdate')
        batchname=request.POST.get('batch')
        batch_name=batch.objects.get(id=batchname)
        batchname=mytask()
        batchname.mytask=batch_name
        mytask(taskbatch=batch_name,title=task,added_date=cdate,task_file=cfile).save()
    return render(request,'thirdapp/fetask.html',md)