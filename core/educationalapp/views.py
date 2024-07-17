from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'registration/login.html')

def signin(request):
    return render(request, 'registration/signin.html')

def signinfavorite(request):
    return render(request, 'registration/signinfavorite.html')

def subscription(request):
    return render(request, 'registration/subscription.html')

def congrateRegister(request):
    return render(request, 'registration/congrateRegister.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def courses(request):
    return render(request, 'courses.html')

def course(request):
    return render(request, 'course.html')

def userdashboard(request):
    return render(request, 'adminPanels/userdashboard.html')
