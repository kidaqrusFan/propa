from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "pages/home.html", {})

def detail(request):
    return render(request, "pages/detail.html", {})

def detail1(request):
     return render(request, "pages/detail1.html", {})


def detail2(request):
    return render(request, "pages/detail2.html", {})


def detail3(request):
    return render(request, "pages/detail3.html", {})

def detail4(request):
    return render(request, "pages/detail4.html", {})

def detail5(request):
    return render(request, "pages/detail5.html", {})

def detail6(request):
    return render(request, "pages/detail6.html", {})

def about(request):
    return render(request, "pages/about.html", {})

def property(request):
    return render(request, "pages/property.html", {})


