from django.db import models

# Create your models here.

#Table for todo app
# task_title for Task Title
# task_status for task is completed or not 
class Task(models.Model):
    task_title=models.CharField(max_length=200,blank=True,null=True)
    task_status=models.BooleanField(default=False, blank=True,null=True)
    def __str__(self):
        return self.task_title