from django.db import models


class DjangoClasses(models.Model):
    title = models.CharField(max_length=100, default="", blank=True)
    course_number = models.IntegerField(default="", blank=True)
    instructor_name = models.CharField(max_length=60, default="", blank=True)
    duration = models.FloatField(max_length=10, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
