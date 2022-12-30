from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to="student/image", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"