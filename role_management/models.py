from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CustomUser

# exit role such as student, ...
class Role(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True,
        verbose_name=_("Name")
    )
    short_name = models.CharField(
        max_length=20,
        verbose_name=_("Short Name")
    )
    
    description = models.TextField(
        verbose_name=_("Description")
    )

    def __str__(self):
        return self.name
    
# define overall permissions for course
class CoursePermission(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True,
        verbose_name=_("Name")
        )
    
    code_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Code Name")
        )
    
    description = models.TextField(
        verbose_name=_("Description")
    )

    def __str__(self):
        return self.name
    
# Model representing a many-to-many relationship between roles and permissions
class RolePermission(models.Model):
    Role = models.ForeignKey(
        Role,
        verbose_name=_("Role"),
        on_delete=models.CASCADE)
    
    course_permission = models.ForeignKey(
        CoursePermission, 
        verbose_name=_("Course Permission"),
        on_delete=models.CASCADE)
    
# RoleAssignment model represents the assignment of a role to a related user
class RoleAssignment(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name=_("Id")
    )

    user = models.ForeignKey(
        CustomUser, 
        verbose_name=_("User"),
        on_delete=models.CASCADE, default=1
    )

    role = models.ForeignKey(
        Role, 
        verbose_name=_("Role"),
        on_delete=models.CASCADE 
    )

    name = models.CharField(
        max_length=50,
        verbose_name=_("Name")    
    )

    # Status of the role assignment (either "active" or "suspended")
    status = models.CharField(
        max_length=10, 
        verbose_name=_("Status"),
        choices=[('active', 'Active'), ('suspended', 'Suspended')]
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At")
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated At")
    )

# when role=student and role assignment occur to user then set this addition details
class StudentMoreDetails(models.Model):
    role_assignemnt = models.OneToOneField(
        RoleAssignment,
        verbose_name=_("Role Assignment"),
        primary_key=True,
        on_delete=models.CASCADE
    )

    resume = models.FileField(
        upload_to='resumes/', 
        verbose_name=_("Resume"),
        blank=True, 
        null=True
    )

    father_name = models.CharField(
        max_length=255,
        verbose_name=_("Father Name")
    )

    mother_name = models.CharField(
        max_length=255,
        verbose_name=_("Mother Name")
    )

    home_number = models.CharField(
        max_length=20,
        verbose_name=_("Home Number"))
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated At")
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At")
    )

# when role=Manager and role assignment occur to user then set this addition details
class ManagerMoreDetails(models.Model):
    role_assignment = models.OneToOneField(
        RoleAssignment, 
        verbose_name=_("Role Assignment"),
        primary_key=True,
        on_delete=models.CASCADE
    )

    resume = models.FileField(
        upload_to='resumes/', 
        verbose_name=_("Resume"),
        blank=True, 
        null=True
    )

    expertise = models.TextField(
        verbose_name=_("Expertise"),
        blank=True, 
        null=True
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True
    )

# every user that has role assignment contain level
class RALevel(models.Model):
    role_assignment = models.ForeignKey(
        RoleAssignment, 
        verbose_name=_("Role Assignment"),
        primary_key=True,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=50
    )

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True
    )

    def __str__(self):
        return self.name
