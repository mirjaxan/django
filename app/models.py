from django.db import models



class Selections(models.Choices):
    new = "new", "New"
    in_progress = "in_progress", "In_progress"
    finished = "finished", "Finished"

class Todo(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    is_active = models.BooleanField()
    
    
    
    def __str__(self):
        return self.title