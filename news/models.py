from django.db import models
import datetime
from django.dispatch import receiver
import os


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(upload_to='images', height_field=None, width_field=None, blank=True)
    create_time = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name_plural = "news"


@receiver(models.signals.post_delete, sender=News)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


@receiver(models.signals.pre_save, sender=News)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False
