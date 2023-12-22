from django.shortcuts import render

def wiew_a(request):
    context={
        'materie' : ["Matematica","Italiano","Inglese","Storia","Geografia"]
    }
    return render(request,"wiew_a.html", context)

def wiew_b(request):
    context={
        'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    }
    return render(request,"wiew_b.html", context)

def wiew_c(request):     
    context={
        'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    }
    return render(request,"wiew_c.html", context)

def wiew_d(request):
    context={
        'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    }
    return render(request,"wiew_d.html", context)

def indexVoti(request):
    return render(request,"indexVoti.html")
