from django.db import models
from django.utils.translation import gettext_lazy as _
from individual_course_templates.models import IndividualCourseTemplate
from individual_course_enrollment.models import IndividualCourseEnrolment

# quiz for template related content
class IndividualCourseQuiz(models.Model):
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

    option1 = models.CharField(
        max_length=255, 
        verbose_name=_("Option 1")
    )

    option2 = models.CharField(
        max_length=255, 
        verbose_name=_("Option 2")
    )

    option3 = models.CharField(
        max_length=255, 
        verbose_name=_("Option 3")
    )

    option4 = models.CharField(
        max_length=255, 
        verbose_name=_("Option 4")
    )

    # Define choices for the correct option
    CORRECT_OPTION_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ]
    
    correct_option = models.CharField(
        max_length=10, 
        verbose_name=_("Correct Option"),
        choices=CORRECT_OPTION_CHOICES
    )


    def __str__(self):
        return self.question
    
    def save(self, *args, **kwargs):
        # Ensure that the correct_option points to one of the options
        if self.correct_option not in ['option1', 'option2', 'option3', 'option4']:
            raise ValueError("Correct option must be one of the defined options.")
        super().save(*args, **kwargs)

# quiz scores for every question ( quiz )
class IndividualCourseQuizPoints(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    quiz = models.ForeignKey(
        IndividualCourseQuiz, 
        on_delete=models.CASCADE, 
        verbose_name=_("Quiz")
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
    
# define role assignment answer for related quiz
class IndividualCourseQuizSubmit(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    quiz = models.ForeignKey(
        IndividualCourseQuiz, 
        on_delete=models.CASCADE, 
        verbose_name=_("Quiz")
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