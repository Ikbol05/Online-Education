
from django.db import models
from django.contrib.auth.models import User




class Course(models.Model):
    ''' bu madel kurslarni yaratish kurish uchun '''

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title





class Lesson(models.Model):
    ''' bu model darslar yaratish va ko'rish uchun hamda vazifa berish'''

    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    ''' bu model darslarga izoh qoldirish uchun '''

    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.lesson}'





class Rating(models.Model):
    ''' bu model darslarni baholash uchun '''

    lesson = models.ForeignKey(Lesson, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Rating by {self.user} on {self.lesson}'



class Homework(models.Model):
    ''' o'quvchilar vazifasini junatish uchun model '''

    lesson = models.ForeignKey(Lesson, related_name='assignments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='homework/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Homework by {self.user} for {self.lesson}'