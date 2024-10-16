from django.db import models
from django.utils.translation import gettext_lazy as _
from individual_course_enrollment.models import IndividualCourseEnrolment
from individual_course_lessons.models import IndividualCourseLessons

# every progressbar( lesson contain collection of progresssbar ) has section in it that contain related content
class IndividualCourseContents(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    lessons_id = models.ForeignKey(
        IndividualCourseLessons, 
        verbose_name=_("Lessons Id"),
        on_delete=models.CASCADE
    )

    # in list of courses contents this index tell, what queue this content has.
    index = models.IntegerField(
        verbose_name=_("Index")
    )

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255
    )

    description = models.TextField(
        verbose_name=_("Description")
    )

    score = models.DecimalField(
        verbose_name=_("Score"),
        max_digits=5, 
        decimal_places=2
    )

    def __str__(self):
        return f"faze section name: {self.title}"
    
    def set_index(self, *args, **kwargs):
        if self.pk is None: # Check if the object is being created
            # Get the maximum index value from the existing records
            max_index = IndividualCourseContents.objects.aggregate(models.Max('index'))
            self.index = (max_index or 0) + 1 # Increment by 1, default to 1 if no records exist
        super().save(*args, **kwargs)

# model for user that complete contents ( single progressbar )
class IndividualCourseContentsComplete(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    contents = models.ForeignKey(
        IndividualCourseContents, 
        verbose_name=_("Lessons"),
        on_delete=models.CASCADE
    )

    individual_course_enrollment = models.ForeignKey(
        IndividualCourseEnrolment, 
        on_delete=models.CASCADE
    )

    created_at = models.DateField(
        verbose_name=_("Created At"),
        auto_now_add=False
    )
