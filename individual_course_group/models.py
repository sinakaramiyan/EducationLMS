from django.db import models
from django.utils.translation import gettext_lazy as _

# in individual course this model stand for learning path that contain related courses
class IndividualCourseGroup(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255
    )

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True
    )

    start_date = models.DateField(
        verbose_name=_("Start Date")
    )

    end_date = models.DateField(
        verbose_name=_("End Date"),
        null=True
    )

    edit_date = models.DateTimeField(
        verbose_name=_("Edit Date"),
        auto_now=True
    )

    visible = models.BooleanField(
        verbose_name=_("Visible"),
        default=False
    )

    enable_completed = models.BooleanField(
        verbose_name=_("Enable Completed"),
        default=False
    )

    def __str__(self):
        return self.title