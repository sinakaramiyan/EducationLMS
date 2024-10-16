from django.db import models
from django.utils.translation import gettext_lazy as _
from individual_course.models import IndividualCourse
from individual_course_enrollment.models import IndividualCourseEnrolment

# chapter means steps that require for pass individual course
class IndividualCourseChapter(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    individual_course = models.ForeignKey(
        IndividualCourse, 
        verbose_name=_("Individual Course"),
        on_delete=models.CASCADE
    )

    # in list of course chapters this index tell, what queue this chapter has.
    index = models.IntegerField()

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
        return self.title
    
    def set_index(self, *args, **kwargs):
        if self.pk is None: # Check if the object is being created
            # Get the maximum index value from the existing records
            max_index = IndividualCourseChapter.objects.aggregate(models.Max('index'))
            self.index = (max_index or 0) + 1 # Increment by 1, default to 1 if no records exist
        super().save(*args, **kwargs)

# model for enrollment user that complete chapter
class IndividualCourseChapterComplete(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    chapter = models.ForeignKey(
        IndividualCourseChapter, 
        verbose_name=_("Chapter"),
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