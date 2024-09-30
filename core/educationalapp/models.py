from django.db import models

class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='', blank=True, null=True)
    firstaccess = models.DateTimeField(auto_now_add=True)
    lastaccess = models.DateTimeField(auto_now=True)
    currentlogin = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} - {self.lastname}"

# notification related to the user
class notification(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    active_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname}{self.lastname} - {self.title}"

class role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

class permission(models.Model):
    name = models.CharField(max_length=50, unique=True)
    codename = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
# Model representing a many-to-many relationship between roles and permissions
class rolePermission(models.Model):
    role = models.ForeignKey(role, on_delete=models.CASCADE)
    permission = models.ForeignKey(permission, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.role.name} - {self.permission.name}"

# RoleAssignment model represents the assignment of a role to a related user
class roleAssignment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    role = models.ForeignKey(role, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # Status of the role assignment (either "active" or "suspended")
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('suspended', 'Suspended')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# when role=student and role assignment occur to user then set this addition details
class student_more_details(models.Model):
    id = models.AutoField(primary_key=True)
    RA_id = models.ForeignKey(roleAssignment, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)
    home_number = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

# when role=admins( all of them ) and role assignment occur to user then set this addition details
class teacher_more_details(models.Model):
    id = models.AutoField(primary_key=True)
    RA_id = models.ForeignKey(roleAssignment, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    expertise = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# every user that has role assignment contain this model
class RA_level(models.Model):
    RA_id = models.ForeignKey(roleAssignment, on_delete=models.CASCADE)
    level_name = models.CharField(max_length=50)
    level_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)