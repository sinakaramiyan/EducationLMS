from django.db import models

#########################
# role assignment process
#########################

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
class studentMoreDetails(models.Model):
    id = models.AutoField(primary_key=True)
    RA_id = models.ForeignKey(roleAssignment, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)
    home_number = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

# when role=admins( all of them ) and role assignment occur to user then set this addition details
class teacherMoreDetails(models.Model):
    id = models.AutoField(primary_key=True)
    RA_id = models.ForeignKey(roleAssignment, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    expertise = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# every user that has role assignment contain this model
class RALevel(models.Model):
    RA_id = models.ForeignKey(roleAssignment, on_delete=models.CASCADE)
    level_name = models.CharField(max_length=50)
    level_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


######################################
# subscription process for student use
######################################

# describe duration of plan
class subscriptionPlan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    duration = models.CharField(max_length=20, choices=[
        ('3 months', '3 months'),
        ('6 months', '6 months'),
        ('1 year', '1 year')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # active status
    active_status = models.BooleanField(default=True)
    activated_at = models.DateTimeField(auto_now_add=True)
    deactivated_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name

class course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    course_level = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ])
    start_date = models.DateField()
    end_date = models.DateField()
    edit_date = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)
    enablecompletion = models.BooleanField(default=False)
    completionnotify = models.BooleanField(default=False)

# every plan has courses with their price mount that can participate in it
class subscriptonCoursePlan(models.Model):
    id = models.AutoField(primary_key=True)
    subscription_plan_id = models.ForeignKey(subscriptionPlan, on_delete=models.CASCADE)
    course_id = models.ForeignKey(course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # active status
    active_status = models.BooleanField(default=True)
    activated_at = models.DateTimeField(auto_now_add=True)
    deactivated_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name

class subscriptionDiscount(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    code = models.CharField(max_length=50, unique=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)

    # active status
    active_status = models.BooleanField(default=True)
    activated_at = models.DateTimeField(auto_now_add=True)
    deactivated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

# acitve subscription plan for user
class subscriptionInPlan(models.Model):
    RA_id = models.OneToOneField(roleAssignment, on_delete=models.CASCADE, primary_key=True)
    subscription_course_plan_id = models.ForeignKey(subscriptonCoursePlan, on_delete=models.CASCADE)
    discount_id = models.ForeignKey(subscriptionDiscount, on_delete=models.CASCADE)

    payment_type = models.CharField(max_length=50)
    payment_code = models.CharField(max_length=50)
    payment_date = models.DateField()
    payment_after_discount = models.DecimalField(max_digits=10, decimal_places=2) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2) 
    discount_price = models.DecimalField(max_digits=10, decimal_places=2) 
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    downgraded_to_plan_id = models.ForeignKey(subscriptonCoursePlan, on_delete=models.CASCADE, null=True, blank=True, related_name='downgraded_plan')
    downgraded_at = models.DateTimeField(null=True, blank=True)

    upgrade_to_plan_id = models.ForeignKey(subscriptonCoursePlan, on_delete=models.CASCADE, null=True, blank=True, related_name='upgraded_plan')
    upgraded_at = models.DateTimeField(null=True, blank=True)

    renewed_subscription_id = models.ForeignKey(subscriptonCoursePlan, on_delete=models.CASCADE, null=True, blank=True, related_name='renewed_subscription')
    renewed_at = models.DateTimeField(null=True, blank=True)


# history of subscription for users
class subscriptionInPlanHisotry(models.Model):
    RA_id = models.OneToOneField(roleAssignment, on_delete=models.CASCADE, primary_key=True)
    subscription_course_plan_id = models.ForeignKey(subscriptonCoursePlan, on_delete=models.CASCADE)

    payment_type = models.CharField(max_length=255)
    payment_code = models.CharField(max_length=255) 
    payment_date = models.DateTimeField() 
    payment_after_discount = models.DecimalField(max_digits=10, decimal_places=2) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField() 

###############
# course enroll
###############

# set role for course 
class courseEnroll(models.Model):
    id = models.AutoField(primary_key=True)
    RA_id = models.ForeignKey(roleAssignment, on_delete=models.CASCADE)
    course_id = models.ForeignKey(course, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    enroll = models.BooleanField(default=False)
    status = models.CharField(max_length=20)
    enroll_period = models.IntegerField()
    enroll_start_date = models.DateField()
    enroll_end_date = models.DateField()
    password = models.CharField(max_length=255)
    expire_notify = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

# when role for course created then role assignment user can participate in course with related role 
class RAEnrollment(models.Model):
    id = models.AutoField(primary_key=True)
    RA_id = models.ForeignKey(roleAssignment, on_delete=models.CASCADE)
    course_enroll_id = models.ForeignKey(courseEnroll, on_delete=models.CASCADE)

    status = models.CharField(max_length=20)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    time_expiration = models.DateTimeField(auto_now=True)

