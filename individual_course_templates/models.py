from django.db import models
from django.utils.translation import gettext_lazy as _
from individual_course_contents.models import IndividualCourseContents

# every content ( single progressbar ) have plenty of content that been save in this model
class IndividualCourseTemplate(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    contents = models.ForeignKey(
        IndividualCourseContents,
        verbose_name=_("Contents"), 
        on_delete=models.CASCADE
    )

    # in list of template this index tell, what queue this template has.
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

    # contain html content
    template_content = models.TextField()  # or use custom models.HTMLField()

    next_template = models.BooleanField(
        verbose_name=_("Next Template"),
        default=False
    )

    def __str__(self):
        return self.title
    
    def set_index(self, *args, **kwargs):
        if self.pk is None: # Check if the object is being created
            # Get the maximum index value from the existing records
            max_index = IndividualCourseContents.objects.aggregate(models.Max('index'))
            self.index = (max_index or 0) + 1 # Increment by 1, default to 1 if no records exist
        super().save(*args, **kwargs)
    
    def check_next_template(self, *args, **kwargs):
        if self.pk is None:
            max_index = IndividualCourseContents.objects.aggregate(models.Max('index'))
            if self.index == max_index :
                self.next_template = True
            else:
                self.next_template = False

    
# define type for template in content
class columnType(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )
    
    templates = models.ForeignKey(
        IndividualCourseTemplate, 
        verbose_name=_("Template"),
        on_delete=models.CASCADE
    )

    TYPE_CHOICES = [
        ('quiz', _('Quiz')),
        ('shortquiz', _('ShortQuiz')),
        ('textbook', _('TextBook')),
        # Add more types as needed
    ]

    type = models.CharField(
        max_length=50, 
        choices=TYPE_CHOICES
    )