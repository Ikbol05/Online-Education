from django.contrib import admin
from . models import Comment, Course, Rating, Lesson
# Register your models here.

'''

Modellarni admin panelga registratsiya qilish

'''

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Rating)