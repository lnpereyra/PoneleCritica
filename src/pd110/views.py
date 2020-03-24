from django.shortcuts import render

# Create your views here.
def about(request):
    
    return render(request, "about.html", {})

def cata(request):

    return render(request, "cata.html", {})

def catb(request):

    return render(request, "catb.html", {})

