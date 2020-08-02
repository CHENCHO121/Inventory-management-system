from django.shortcuts import render,redirect,get_object_or_404
from .models import Desktop,Laptop,Mobile
from .forms import Laptopform,Mobileform,Desktopform

def index(request):
    return render(request,'index.html')

def display_desktop(request):
    items=Desktop.objects.all()
    context={
        'item':items,
        'header':'desktops'
    }
    return render(request,'index.html',context)

def display_laptop(request):
    items=Laptop.objects.all()
    context={
        'item':items,
        'header':'laptops'
    }
    return render(request,'index.html',context)

def display_mobile(request):
    items=Mobile.objects.all()
    context={
        'item':items,
        'header':'mobiles'
    }
    return render(request,'index.html',context)


def add_device(request,cls):
    if request.method=="POST":
        form=cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=cls()
        return render(request,'add_device.html',{'form':form})


def add_laptop(request):
    return add_device(request,Laptopform)

def add_desktop(request):
    return add_device(request,Desktopform)

def add_mobile(request):
    return add_device(request,Mobileform)

def edit_device(request,pk,model,cls):
    item=get_object_or_404(model,pk=pk)
    if request.method=="POST":
        form=cls(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Laptopform(instance=item)
        return render(request,'edit_device.html',{'form':form})

def edit_laptop(request,pk):
    return edit_device(request,pk,Laptop,Laptopform)

def edit_mobile(request,pk):
    return edit_device(request,pk,Mobile,Mobileform)

def edit_desktop(request,pk):
    return edit_device(request,pk,Desktop,Desktopform)

def delete_device(request,pk,model):
    item = model.objects.get(pk=pk)
    item.delete()
    return redirect('/')

def delete_laptop(request,pk):
    return delete_device(request,pk,Laptop)

def delete_desktop(request,pk):
    return delete_device(request,pk,Desktop)

def delete_mobile(request,pk):
    return delete_device(request,pk,Mobile)

