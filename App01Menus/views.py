from django.shortcuts import render
from .models import *
# Create your views here.

def Menu(request):
    familias = Familia.objects.all()
    productos = Producto.objects.all()
    familias_no_vacias=()
    y=list(familias_no_vacias)
    for i in familias:
        count=0
        for j in productos:
            if j.tipo.name==i.name:
                count=+1
        if count!=0:
            y.append(i.name)

    print('Familias ===> ', y)
    qr = Website.objects.get(pk=1)
    
    return render(request,'App01Menus/Menu.html',locals())

def productDetail(request,pk):
    producto = Producto.objects.get(pk=pk)
    return render(request,'App01Menus/Detail.html',locals())