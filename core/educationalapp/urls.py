from django.urls import path
from .views import home, login, signin, signinfavorite, testimonial, courses,course, course,monacoeditor, lessoncompletestroke, lessoncompleteleague,  courseintroduction, dashboard, profile, setting, resetpassword, calendar, congrateRegister, subscription, modules, lesson, lessoncomplete, userhomecourse, moodlestudentcourses, moodlestudentcoursedetail,moodlestudentcourse,moodlestudentweek,moodlestudentprofile, moodlesblogblogs

urlpatterns = [
    path('', home, name='home'),
    path('login/', login , name='login'),
    path('signin/', signin , name='signin'),
    path('signinfavorite/', signinfavorite , name='signinfavorite'),
    path('testimonial/', testimonial , name='testimonial'),
    path('courseintroduction/', courseintroduction , name='courseintroduction'),
    path('congrateRegister/', congrateRegister , name='congrateRegister'),
    path('subscription/', subscription , name='subscription'),   

    # start admin

    path('dashboard/', dashboard , name='dashboard'),
    path('dashboard/profile/', profile , name='profile'),
    path('dashboard/calendar/', calendar , name='calendar'),
    path('dashboard/resetpassword/', resetpassword , name='resetpassword'),
    path('dashboard/setting/', setting , name='setting'),

    # end admin

    # start brilliant

    path('brilliant/home/', userhomecourse , name='userhomecourse'),
    path('brilliant/courses/', courses , name='courses'),
    path('brilliant/modules/learning_path', modules , name='modules'),   
    path('brilliant/courses/coursename', course , name='course'),   
    path('brilliant/courses/coursename/lesson', lesson , name='lesson'),
    path('brilliant/courses/coursename/lesson/lessoncomplete', lessoncomplete , name='lessoncomplete'),
    path('brilliant/courses/coursename/lesson/lessoncompletestroke', lessoncompletestroke , name='lessoncompletestroke'),
    path('brilliant/courses/coursename/lesson/lessoncompleteleague', lessoncompleteleague , name='lessoncompleteleague'),

    # end brilliant

    # start moodle

    path('meetbased/student/courses/', moodlestudentcourses , name='moodlestudentcourses'),
    path('meetbased/student/coursedetail/', moodlestudentcoursedetail , name='moodlestudentcoursedetail'),
    path('meetbased/student/course/', moodlestudentcourse , name='moodlestudentcourse'),
    path('meetbased/student/week/', moodlestudentweek , name='moodlestudentweek'),
    path('meetbased/student/profile/', moodlestudentprofile , name='moodlestudentprofile'),
    path('meetbased/blog/blogs/', moodlesblogblogs , name='moodlesblogblogs'),

    # end moodle
    
    path('monaco-editor', monacoeditor , name='monacoeditor'),
]