from django.contrib import admin
from .models import IndividualShortQuiz, IndividualShortQuizOptions, IndividualShortQuizPoints, IndividualShortQuizSubmit

admin.site.register(IndividualShortQuiz)

admin.site.register(IndividualShortQuizOptions)

admin.site.register(IndividualShortQuizPoints)

admin.site.register(IndividualShortQuizSubmit)