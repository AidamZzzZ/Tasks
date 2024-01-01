from django.db import models

PRIORITY_STATUS_CHOICES = (
    ('Pendiente', 'Pendiente'),
    ('Completado', 'Completado')
)

class Task(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    due_date = models.DateTimeField()
    priority = models.IntegerField()
    status = models.CharField(max_length=11, choices=PRIORITY_STATUS_CHOICES)
    
    def __str__(self):
        return self.title
    
class List(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    tasks = models.ManyToManyField(Task)
