from django.urls import path
from .views import home, login, signin, signinfavorite, testimonial, courses, course, userdashboard, congrateRegister, subscription

urlpatterns = [
    path('', home, name='home'),
    path('login/', login , name='login'),
    path('signin/', signin , name='signin'),
    path('signinfavorite/', signinfavorite , name='signinfavorite'),
    path('testimonial/', testimonial , name='testimonial'),
    path('courses/', courses , name='courses'),
    path('course/', course , name='course'),
    path('user-dashboard/', userdashboard , name='userdashboard'),
    path('congrateRegister/', congrateRegister , name='congrateRegister'),
    path('subscription/', subscription , name='subscription'),   
]