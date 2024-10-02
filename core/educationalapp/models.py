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

    def __str__(self):
        return f"{self.firstname}-{self.lastname} => {self.role.name}"

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

    def __str__(self):
        return f"{self.RA_id.user.firstname}-{self.RA_id.user.lastname} => level: {self.level_name}"


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

    def __str__(self):
        return f"{self.title}({self.title})"

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

##################
# course automatic
##################

# in automatic course this model stand for learning path that contain courses
class automaticCourseGroup(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    edit_date = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)
    enable_completion = models.BooleanField(default=False)

    def __str__(self):
        return f"course group: {self.title}"

# model for user that complete group
class automaticCourseGroupComplete(models.Model):
    id = models.AutoField(primary_key=True)
    course_group_id = models.ForeignKey(automaticCourseGroup, on_delete=models.CASCADE)
    RA_enrollment_id = models.ForeignKey(RAEnrollment, on_delete=models.CASCADE)
    time_modified = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"The course_group {self.course_group_id.title} completed with {self.RA_enrollment_id.RA_id.user.firstname}-{self.RA_enrollment_id.RA_id.user.lastname} at {self.time_modified}"

# represent course in learning path
class automaticCourse(models.Model):
    id = models.AutoField(primary_key=True)
    course_group_id = models.ForeignKey(automaticCourseGroup, on_delete=models.CASCADE)
    # in list of learning path this index tell, what queue this course has.
    index = models.IntegerField()
    prerequisite = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True, parent_link=True)
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    edit_date = models.DateField(auto_now=True)
    visible = models.BooleanField(default=True)
    language = models.CharField(max_length=10)
    enable_completion = models.BooleanField(default=False)
    completion_notify = models.BooleanField(default=False)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"course title: {self.title}"

# model for user that complete course
class automaticCourseComplete(models.Model):
    id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(automaticCourse, on_delete=models.CASCADE)
    RA_enrollment_id = models.ForeignKey(RAEnrollment, on_delete=models.CASCADE)
    time_modified = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"The course {self.course_id.title} completed with {self.RA_enrollment_id.RA_id.user.firstname}-{self.RA_enrollment_id.RA_id.user.lastname} at {self.time_modified}"

# faze means steps that require for pass course
class automaticCourseFaze(models.Model):
    id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(automaticCourse, on_delete=models.CASCADE)
    # in list of courses faze this index tell, what queue this faze has.
    index = models.IntegerField()
    title = models.CharField(max_length=255)
    sub_name = models.CharField(max_length=255, blank=True, null=True)
    faze_intro_title = models.CharField(max_length=255)
    faze_intro_content = models.TextField()
    faze_review_title = models.CharField(max_length=255)
    faze_review_content = models.TextField()
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"faze name: {self.title}"


# model for user that complete faze
class automaticCourseFazeComplete(models.Model):
    id = models.AutoField(primary_key=True)
    faze_id = models.ForeignKey(automaticCourseFaze, on_delete=models.CASCADE)
    RA_enrollment_id = models.ForeignKey(RAEnrollment, on_delete=models.CASCADE)
    time_modified = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"The faze {self.faze_id.title} completed with {self.RA_enrollment_id.RA_id.user.firstname}-{self.RA_enrollment_id.RA_id.user.lastname} at {self.time_modified}"

# in every faze we have collection of group that in ui can see as slaty progressbar
class automaticCourseFazeGroup(models.Model):
    id = models.AutoField(primary_key=True)
    faze_id = models.ForeignKey(automaticCourseFaze, on_delete=models.CASCADE)
    # in list of courses faze group this index tell, what queue this faze group has.
    index = models.IntegerField()
    title = models.CharField(max_length=255)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"faze group name: {self.title}"
    
# model for user that complete group
class automaticCourseFazeGroupComplete(models.Model):
    id = models.AutoField(primary_key=True)
    faze_group_id = models.ForeignKey(automaticCourseFazeGroup, on_delete=models.CASCADE)
    RA_enrollment_id = models.ForeignKey(RAEnrollment, on_delete=models.CASCADE)
    time_modified = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"The group faze {self.faze_group_id.title} completed with {self.RA_enrollment_id.RA_id.user.firstname}-{self.RA_enrollment_id.RA_id.user.lastname} at {self.time_modified}"
    
# every progressbar( group contain collection of progresssbar ) has section in it that contain related content
class automaticCourseFazeGroupSection(models.Model):
    id = models.AutoField(primary_key=True)
    faze_group_id = models.ForeignKey(automaticCourseFazeGroup, on_delete=models.CASCADE)
    # in list of courses faze group section this index tell, what queue this faze group section has.
    index = models.IntegerField()
    title = models.CharField(max_length=255)
    section_type = models.CharField(max_length=50)
    n_the_section = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"faze section name: {self.title}"

# model for user that complete faze section ( individual progressbar )
class automaticCourseFazeGroupComplete(models.Model):
    id = models.AutoField(primary_key=True)
    faze_group_section_id = models.ForeignKey(automaticCourseFazeGroupSection, on_delete=models.CASCADE)
    RA_enrollment_id = models.ForeignKey(RAEnrollment, on_delete=models.CASCADE)
    time_modified = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"The group faze section {self.faze_group_section_id.title} completed with {self.RA_enrollment_id.RA_id.user.firstname}-{self.RA_enrollment_id.RA_id.user.lastname} at {self.time_modified}"

# every faze section ( individual progressbar ) have plenty of content that been save in this model
class automaticCourseFazeGroupSectionContentTemplate(models.Model):
    id = models.AutoField(primary_key=True)
    faze_group_section_id = models.ForeignKey(automaticCourseFazeGroupSection, on_delete=models.CASCADE)
    # in list of courses faze group section content this index tell, what queue this faze group section content has.
    index = models.IntegerField()
    title = models.CharField(max_length=255)
    # contain html content
    section_content = models.TextField()  # or use custom models.HTMLField()
    has_next_btn = models.BooleanField(default=False)

    def __str__(self):
        return self.section_content
    
# define type for content in faze section content template
class columnType(models.Model):
    id = models.AutoField(primary_key=True)
    template_id = models.ForeignKey(automaticCourseFazeGroupSectionContentTemplate, on_delete=models.CASCADE)
    TYPE_CHOICES = [
        ('question', 'Question'),
        ('content', 'Number'),
        ('data', 'Data'),
        # Add more choices as needed
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.template_id.title} - {self.type}"

# quiz for template related content
class templateQuiz(models.Model):
    id = models.AutoField(primary_key=True)
    template_id = models.ForeignKey(automaticCourseFazeGroupSectionContentTemplate, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255)

    def __str__(self):
        return self.question

# quiz score for every question ( quiz )
class quizPoints(models.Model):
    id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey(templateQuiz, on_delete=models.CASCADE)
    points_title = models.CharField(max_length=255)
    points_value = models.IntegerField()

    def __str__(self):
        return f"{self.quiz_id.question} - score: {self.points_value}"
    
# define user answer for related quiz
class submitQuiz(models.Model):
    id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey(templateQuiz, on_delete=models.CASCADE)
    RA_enrollment_id = models.ForeignKey(RAEnrollment, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    time_modified = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.is_correct

# short quiz for template related content
class templateShorQuiz(models.Model):
    id = models.AutoField(primary_key=True)
    template_id = models.ForeignKey(automaticCourseFazeGroupSectionContentTemplate, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return f"{self.template_id.title} - question: {self.question}"
    
# options for short quiz
class shortQuizOptions(models.Model):
    id = models.AutoField(primary_key=True)
    short_quiz_id = models.ForeignKey(templateShorQuiz, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.is_correct


# short quiz score for every question ( quiz )
class quizPoints(models.Model):
    id = models.AutoField(primary_key=True)
    short_quiz_id = models.ForeignKey(templateShorQuiz, on_delete=models.CASCADE)
    points_title = models.CharField(max_length=255)
    points_value = models.IntegerField()

    def __str__(self):
        return f"{self.short_quiz_id.question} - score: {self.points_value}"
    
# define user answer for related quiz
class submitShortQuiz(models.Model):
    id = models.AutoField(primary_key=True)
    short_quiz_id = models.ForeignKey(templateShorQuiz, on_delete=models.CASCADE)
    RA_enrollment_id = models.ForeignKey(RAEnrollment, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    time_modified = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.is_correct