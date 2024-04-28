from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Curriculum(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.title}, {self.description}, {self.start_date}, {self.end_date}'


class DayLog(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, null=True)
    day_number = models.PositiveIntegerField(null=True)
    notepad = models.TextField(null=True, blank=True)
    highlight = models.TextField(null=True, blank=True)
    blunder = models.TextField(null=True, blank=True)
    references = models.JSONField(null=True)
    subtopics = models.JSONField(null=True)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True)

    def save(self, *args, **kwargs):
        
        # Calculate the day number based on the number of existing logs for this curriculum
        if not self.pk:
            self.day_number = DayLog.objects.filter(curriculum=self.curriculum).count() + 1
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.curriculum.title}: {self.title}'