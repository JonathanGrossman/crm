from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from datetime import datetime

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    create_time = models.DateTimeField(default=datetime.now, blank=True)
    last_update_time = models.DateTimeField(default=datetime.now, blank=True)
    existing_skills = ArrayField(JSONField())
    desired_skills = ArrayField(JSONField())
    interested_courses = ArrayField(JSONField())
    def __str__(self):
        full_name = self.last_name + ", " + self.first_name
        return full_name