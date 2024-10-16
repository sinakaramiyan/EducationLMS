from django.db import models
from django.utils.translation import gettext_lazy as _
from role_management.models import Role, RoleAssignment
from individual_course.models import IndividualCourse
from django.contrib.auth.hashers import make_password, check_password

# When role for course assigned then role assignment user can participate in course with related assigned role 
class IndividualCourseEnrolment(models.Model):
    id = models.AutoField(
        verbose_name=_("ID"),
        primary_key=True
    )

    role_assignment = models.ForeignKey(
        RoleAssignment, 
        verbose_name=_("Role Assignment"),
        on_delete=models.CASCADE
    )

    individual_course = models.ForeignKey(
        IndividualCourse,
        verbose_name=_("Individual Course"),
        on_delete=models.CASCADE
    )

    completed_course = models.BooleanField(
        verbose_name=_("Completed Course"),
    )

    status = models.BooleanField(
        verbose_name=_("Enroll"),
        default=False
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True
    )

    modified_at = models.DateTimeField(
        verbose_name=_("Modified At"),
        auto_now=True
    )

    expirate = models.BooleanField(
        verbose_name=_("Expirate"),
        default=False
    )