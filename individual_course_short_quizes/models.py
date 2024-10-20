from django.db import models
from django.utils.translation import gettext_lazy as _
from individual_course_templates.models import IndividualCourseTemplate
from individual_course_enrollment.models import IndividualCourseEnrolment

# short quiz for template related content
class IndividualShortQuiz(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    template = models.ForeignKey(
        IndividualCourseTemplate, 
        verbose_name=_("Individual Course Template"),
        on_delete=models.CASCADE
    )

    question = models.TextField(
        verbose_name=_("Question")
    )

    def __str__(self):
        return self.question
    
# answer options for short quiz
class IndividualShortQuizOptions(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    short_quiz = models.ForeignKey(
        IndividualShortQuiz, 
        verbose_name=_("Individual Short Quiz"),
        on_delete=models.CASCADE
    )

    text = models.CharField(
        verbose_name=_("Option Text"),
        max_length=255
    )

    is_correct = models.BooleanField(
        verbose_name=_("Is Correct"),
        default=False
    )

    def __str__(self):
        return self.text

# short quiz score for every question ( short quiz )
class IndividualShortQuizPoints(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    short_quiz = models.ForeignKey(
        IndividualShortQuiz, 
        verbose_name=_("Individual Short Quiz"),
        on_delete=models.CASCADE
    )

    points_title = models.CharField(
        verbose_name=_("Points Title"),
        max_length=50
    )

    points_value = models.IntegerField(
        verbose_name=_("Points Value")
    )

    def __str__(self):
        return f"{self.points_title}: {self.points_value}"
    
# define user answer for related short quiz
class IndividualShortQuizSubmit(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    short_quiz = models.ForeignKey(
        IndividualShortQuiz, 
        verbose_name=_("Individual Short Quiz"),
        on_delete=models.CASCADE
    )

    individual_course_enrollment = models.ForeignKey(
        IndividualCourseEnrolment,
        verbose_name=_("Individual Course Enrolment"),
        on_delete=models.CASCADE
    )

    is_correct = models.BooleanField(
        verbose_name=_("Is Correct"),
        default=False
    )

    created_at = models.DateField(
        verbose_name=_("Created At"),
        auto_now_add=True
    )

    modified_at = models.DateField(
        verbose_name=_("Modified At"),
        auto_now=True
    )

    score = models.DecimalField(
        verbose_name=_("Score"),
        max_digits=5, 
        decimal_places=2,
        default=0.00
    )

    def __str__(self):
        return self.is_correct