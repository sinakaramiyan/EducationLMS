from django.urls import path
from .views import home, login, signin, signinfavorite, testimonial, course,monacoeditor, courseintroduction, dashboard, profile, setting, resetpassword, calendar, congrateRegister, subscription
from .views import modules, lesson, lessoncomplete, userhomecourse, lessoncompletestroke, lessoncompleteleague, courses,course
from .views import moodlegeneralcourses, moodlegeneralcoursedetail
from .views import moodlestudentcourse,moodlestudentweek,moodlestudentprofile 
from .views import moodlesblogblogs, moodlesblogcategories, moodlesblogcategorypage, moodlesblogsingleblog
from .views import moodlesforumforum, moodlesforumforums
from .views import moodleteachercourse, moodleteacherweek, moodleteacherprofile
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

    path('meetbased/courses/', moodlegeneralcourses , name='moodlegeneralcourses'),
    path('meetbased/coursedetail/', moodlegeneralcoursedetail , name='moodlegeneralcoursedetail'),
    path('meetbased/student/course/', moodlestudentcourse , name='moodlestudentcourse'),
    path('meetbased/student/week/', moodlestudentweek , name='moodlestudentweek'),
    path('meetbased/student/profile/', moodlestudentprofile , name='moodlestudentprofile'),
    path('meetbased/blog/blogs/', moodlesblogblogs , name='moodlesblogblogs'),
    path('meetbased/blog/categories/', moodlesblogcategories , name='moodlesblogcategories'),
    path('meetbased/blog/category/page', moodlesblogcategorypage , name='moodlesblogcategorypage'),
    path('meetbased/blog/blogname', moodlesblogsingleblog , name='moodlesblogsingleblog'),
    path('meetbased/forum/forumname', moodlesforumforum , name='moodlesforumforum'),
    path('meetbased/forums', moodlesforumforums , name='moodlesforumforums'),
    path('meetbased/teacher/course/', moodleteachercourse , name='moodleteachercourse'),
    path('meetbased/teacher/week/', moodleteacherweek , name='moodleteacherweek'),
    path('meetbased/teacher/profile/', moodleteacherprofile , name='moodleteacherprofile'),

    # end moodle
    
    path('monaco-editor', monacoeditor , name='monacoeditor'),
]