from django.db import models
from core.models import CustomUser
from django.utils.translation import gettext_lazy as _

class Notification(models.Model):
    id = models.AutoField(
        verbose_name=_("Id"),
        primary_key=True
    )
    
    user = models.ManyToManyField(
        CustomUser, 
        verbose_name=_("User"),
    )
    
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255
    )

    description = models.TextField(
        verbose_name=_("Description")
    )

    active_status = models.BooleanField(
        verbose_name=_("Active Status"),
        default=False
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True
    )