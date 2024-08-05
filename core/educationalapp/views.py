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

def courseintroduction(request):
    return render(request, 'courseintroduction.html')

def dashboard(request):
    return render(request, 'adminPanels/dashboard.html')

def profile(request):
    return render(request, 'adminPanels/profile.html')

def calendar(request):
    return render(request, 'adminPanels/calendar.html')

def resetpassword(request):
    return render(request, 'adminPanels/resetpassword.html')

def setting(request):
    return render(request, 'adminPanels/setting.html')

def modules(request):
    return render(request, 'courseLearning/modules.html')

def course(request):
    return render(request, 'courseLearning/course.html')

def lesson(request):
    return render(request, 'courseLearning/lesson.html')

def lessoncomplete(request):
    return render(request, 'courseLearning/lessoncomplete.html')

def lessoncompletestroke(request):
    return render(request, 'courseLearning/lessoncompletestroke.html')

def lessoncompleteleague(request):
    return render(request, 'courseLearning/lessoncompleteleague.html')

def userhomecourse(request):
    return render(request, 'userhomecourse.html')

def monacoeditor(request):
    return render(request, 'monacoeditor.html')
    