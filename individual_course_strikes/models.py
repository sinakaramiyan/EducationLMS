from datetime import timedelta, datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CustomUser

DAYS_OF_WEEK = [
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday'),
]

# maintain strike for users in individual course
class IndividualCourseStrike(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    user = models.ForeignKey(
        CustomUser, 
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )

    created_at = models.DateField(
        verbose_name=_("Created At"),
        auto_now_add=True
    )

    modified_at = models.DateField(
        verbose_name=_("Modified At"),
        auto_now=True
    )

    day_name = models.CharField(
        max_length=10, 
        verbose_name=_("Day Name"),
        choices=DAYS_OF_WEEK
    )
    
    battery_status = models.CharField(
        max_length=4, 
        choices=[
            ( 0 , 'zero'),
            ( 1 , 'One'),
            ( 2 , 'Two'),
        ],
        default=0
    )

    # how many day this strike can be active
    length = models.SmallIntegerField(
        verbose_name=_("Length")
    )

    expired_at = models.DateField(
        verbose_name=_("Expired At")
    )

    strike_status = models.CharField(
        max_length=50, 
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('expired', 'Expired'),
        ]
    )

    def __str__(self):
        return self.day_name
    
    def check_expired(self):
        """
        Check if the instance has expired based on the given length and created_at date.
        If expired, set the status to "expired".

        :param instance: The instance to check (e.g. a model instance)
        :param length: The length of time before expiration (e.g. 30 days)
        :return: None
        """
        created_at = self.created_at  # assume created_at is a DateField
        expired_at = created_at + timedelta(days=self.length)

        if datetime.date.today() > expired_at:
            self.strike_status = "expired"

    
# contain history of strikes that user had
class IndividualCourseStrikeHistory(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )

    user = models.ForeignKey(
        CustomUser, 
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )

    created_at = models.DateField(
        verbose_name=_("Created At"),
        auto_now_add=True
    )

    day_name = models.CharField(
        max_length=10, 
        verbose_name=_("Day Name"),
        choices=DAYS_OF_WEEK
    )

    battery_status = models.CharField(
        max_length=4, 
        choices=[
            ( 0 , 'zero'),
            ( 1 , 'One'),
            ( 2 , 'Two'),
        ],
        default=0
    )
    
    expired_at = models.DateField(
        verbose_name=_("Expired At")
    )

    strike_status = models.CharField(
        max_length=50, 
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('expired', 'Expired'),
        ]
    )
