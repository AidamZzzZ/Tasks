from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    due_date = models.DateTimeField()
    priority = models.IntegerField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
