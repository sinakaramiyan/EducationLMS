from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.urls import reverse_lazy
from .models import User
from .forms import UserRegistrationForm, signInForm
from .authentications import EmailBackend
from django.contrib.auth import views, forms

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

def courseintroduction(request):
    return render(request, 'courseintroduction.html')

# start admin

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

# end admin

# start brilliant

def brilliantSignIn(request):
    if request.method == "POST":
        form = signInForm(request.POST)
        print(form)

        print(request.POST.get('username'))
        print(request.POST.get('password'))
        print(form.is_valid)
        if form.is_valid():
            print('1')
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = EmailBackend.authenticate(username=email, password=password)
            if user is not None:
                print('2')
                login(request, user)
                print('3')
                return redirect('/brilliant/home/')
        elif not form.is_valid():
            print('5')
            print(form.errors)
            print('8')
            form.errors['password'] = form.error_class(['رمز عبور با تکرار آن برابر نیست.'])
    else:
        print('6')
        form = signInForm()
    
    print('4')
    return render(request, 'courseLearning/signin.html', {'form': form})

def brilliantSignUp(request):
    # reset form in every refresh and back button
    # password hashing for when save in db
    # show error messages
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                # Create a new user
                user = User(
                    email=email, 
                    password=password1, 
                    first_name=first_name, 
                    last_name=last_name,
                    phone=phone
                )
                user.save()
                resopnse = redirect('/brilliant/signIn')
                return resopnse
            else:
                form.errors['password2'] = form.error_class(['رمز عبور با تکرار آن برابر نیست.'])
    else:
        form = UserRegistrationForm()

    return render(request, 'courseLearning/signUp.html', {'form': form})

def brilliantResetPassword(request):
    return render(request, 'courseLearning/resetPassword.html')

def courses(request):
    return render(request, 'courseLearning/courses.html')

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
    return render(request, 'courseLearning/userhomecourse.html')

# end brilliant

# start moodle

def moodlegeneralcourses(request):
    return render(request, 'meetbased/courses.html')

def moodlegeneralcoursedetail(request):
    return render(request, 'meetbased/coursedetail.html')

def moodlestudentcourse(request):
    return render(request, 'meetbased/student/course.html')

def moodlestudentweek(request):
    return render(request, 'meetbased/student/week.html')

def moodlestudentprofile(request):
    return render(request, 'meetbased/student/profile.html')

def moodlesblogblogs(request):
    return render(request, 'meetbased/blog/blogs.html')

def moodlesblogcategories(request):
    return render(request, 'meetbased/blog/blogCategories.html')

def moodlesblogcategorypage(request):
    return render(request, 'meetbased/blog/blogCategoryPage.html')

def moodlesblogsingleblog(request):
    return render(request, 'meetbased/blog/singleblog.html')

def moodlesforumforum(request):
    return render(request, 'meetbased/forum/forum.html')

def moodlesforumforums(request):
    return render(request, 'meetbased/forum/forums.html')

def moodleteachercourse(request):
    return render(request, 'meetbased/teacher/course.html')

def moodleteacherweek(request):
    return render(request, 'meetbased/teacher/week.html')

def moodleteacherprofile(request):
    return render(request, 'meetbased/teacher/profile.html')

# end moodle

def monacoeditor(request):
    return render(request, 'monacoeditor.html')