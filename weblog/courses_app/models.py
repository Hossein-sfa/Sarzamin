from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.CharField(max_length=50)
    is_finished = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    course_image = models.ImageField(null=True, upload_to='Courses')
    
    def __str__(self):
        return self.title
