from django.db import models

CLASS_NAMES = [
    ('Math', 'Math'), ('Science', 'Science'),
    ('English', 'English'), ('French', 'French'),
    ('Philosophy', 'Philosophy'),
]

class djangoClasses(models.Model):
    title = models.CharField(max_length=60, choices= CLASS_NAMES)
    course_number = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    name = models.TextField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(default=0.00)

    objects = models.Manager()



    def __str__(self):
        return self.title

