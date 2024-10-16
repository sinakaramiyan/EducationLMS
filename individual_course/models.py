from django.db import models
from django.utils.translation import gettext_lazy as _
from individual_course_group.models import IndividualCourseGroup
from role_management.models import Role

# represent individual course in learning path for individual course group
class IndividualCourse(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    individual_course_group = models.ForeignKey(
        IndividualCourseGroup, 
        verbose_name=_("Individual Course Group"),
        on_delete=models.CASCADE
    )

    role = models.ManyToManyField(
        Role,
        verbose_name=_("Role")
    )

    # in list of learning path ( individual course group ) this index tell, what queue this individual course has.
    index = models.IntegerField(
        verbose_name=_("Index")
    )

    prerequisite = models.OneToOneField(
        'self', 
        on_delete=models.CASCADE, 
        verbose_name=_("Prerequisite"),
        null=True, 
        parent_link=True
    )

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255
    )

    description = models.TextField(
        verbose_name=_("Description")
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
            max_index = IndividualCourse.objects.aggregate(models.Max('index'))
            self.index = (max_index or 0) + 1 # Increment by 1, default to 1 if no records exist
        super().save(*args, **kwargs)