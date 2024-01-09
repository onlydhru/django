from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {})
def about(request):
    return render(request, 'pages/About.html', {})

def Registration(request):
    return render(request, 'pages/Registration.html', {})

def Dashboard(request):
    return render(request, 'pages/Dashboard.html', {})

def Contact(request):
    return render(request, 'pages/Contact.html', {})
def Login(request):
    return render(request, 'pages/Login.html', {})
def Base(request):
    return render(request, 'pages/Base.html', {})
def shs(request):
    return render(request, 'pages/shs.html', {})
def college(request):
    return render(request, 'pages/college.html', {})
def basiced(request):
    return render(request, 'pages/basiced.html', {})



