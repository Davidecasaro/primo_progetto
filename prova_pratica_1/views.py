from django.shortcuts import render
import random

# Create your views here.
def index_prova(request):
    return render(request,"index_prova.html")

def media(request):
    var=0
    lista=[]
    i=1
    for i in range(30):
        n=random.randint(1,10)
        lista.append(n)
        var+=n
    var=var/30
    context={
        'lista' : lista,
        'var' : var,
    }
    return render(request,"media.html", context)

def voti(request):
    context={
         'my_dict' : {'stud1': 8, 'stud2': 7,'stud3':3}
    }
    return render(request,"voti.html", context)

def somma(request):
    var1=random.randint(1,10)
    var2=random.randint(1,10)
    var3=var1+var2
    context={
       'var1' : var1,
       'var2' : var2,
       'var3' : var3,
    }
    return render(request, "somma.html", context)
