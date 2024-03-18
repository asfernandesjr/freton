from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CoreModel(models.Model):
    
    def save(self, *args, **kwargs):
        super().full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class BaseModel(CoreModel):
    is_active = models.BooleanField(
        _('is active'),
        default=True
    )
    created_at = models.DateTimeField(
        _('created at'),
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        _('updated at'),
        auto_now=True
    )
    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='created_%(class)ss'
    )
    updated_by = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='updated_%(class)ss'
    )
    
    class Meta:
        abstract = True

