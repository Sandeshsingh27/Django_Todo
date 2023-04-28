from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    complete = models.BooleanField(default=False)
    time=models.DateTimeField(auto_now_add=True, null=True)

# Below function is used to edit the object filed shown in the admin interface
    def __str__(self):
        return self.title