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

def moodlestudentcourses(request):
    return render(request, 'meetbased/student/courses.html')

def moodlestudentcoursedetail(request):
    return render(request, 'meetbased/student/coursedetail.html')

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

# end moodle

def monacoeditor(request):
    return render(request, 'monacoeditor.html')