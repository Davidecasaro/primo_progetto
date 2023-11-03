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
    diz = ['studente1',8,'studente2',7,'studente3',3]
    fstStud=diz[0] 
    sndStud=diz[2]
    trdStud=diz[4]
    fstVoto=diz[1] 
    sndVoto=diz[3]
    trdVoto=diz[5]

    context={
        'fstStud' : fstStud,
        'sndStud' : fstStud,
        'trdStud' : fstStud,
        'fstVoto' : fstVoto,
        'sndVoto' : sndVoto,
        'trdVoto' : trdVoto,
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
