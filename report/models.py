from django.db import models
from django.core.cache import cache
# Create your models here.

SEX_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female")
)

class MissingReport(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    photo = models.ImageField(upload_to="report_image")
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"{self.name} ({self.sex})"
    
    def save(self, *args, **kwargs):
        '''Delete "missing_person_list" form cache when new missing person added'''
        if not self.id:
            if cache.get("missing_person_list"):
                cache.delete("missing_person_list")
        else:
            if cache.get(f"report_{self.id}"):
                cache.delete(f"report_{self.id}")

        super(MissingReport, self).save(*args, **kwargs)

