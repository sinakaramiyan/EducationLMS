from django.urls import path
from .views import home, login, signin, signinfavorite, testimonial, courses,course, course,monacoeditor, lessoncompletestroke, lessoncompleteleague,  courseintroduction, dashboard, profile, setting, resetpassword, calendar, congrateRegister, subscription, modules, lesson, lessoncomplete, userhomecourse

urlpatterns = [
    path('', home, name='home'),
    path('home/', userhomecourse , name='userhomecourse'),
    path('login/', login , name='login'),
    path('signin/', signin , name='signin'),
    path('signinfavorite/', signinfavorite , name='signinfavorite'),
    path('testimonial/', testimonial , name='testimonial'),
    path('courses/', courses , name='courses'),
    path('courseintroduction/', courseintroduction , name='courseintroduction'),
    path('dashboard/', dashboard , name='dashboard'),
    path('dashboard/profile/', profile , name='profile'),
    path('dashboard/calendar/', calendar , name='calendar'),
    path('dashboard/resetpassword/', resetpassword , name='resetpassword'),
    path('dashboard/setting/', setting , name='setting'),
    path('congrateRegister/', congrateRegister , name='congrateRegister'),
    path('subscription/', subscription , name='subscription'),   
    path('modules/learning_path', modules , name='modules'),   
    path('courses/coursename', course , name='course'),   
    path('courses/coursename/lesson', lesson , name='lesson'),
    path('courses/coursename/lesson/lessoncomplete', lessoncomplete , name='lessoncomplete'),
    path('courses/coursename/lesson/lessoncompletestroke', lessoncompletestroke , name='lessoncompletestroke'),
    path('courses/coursename/lesson/lessoncompleteleague', lessoncompleteleague , name='lessoncompleteleague'),
    path('monaco-editor', monacoeditor , name='monacoeditor'),
]