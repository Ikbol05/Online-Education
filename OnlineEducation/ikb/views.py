from rest_framework import viewsets, permissions
from .models import Course, Lesson, Comment, Rating, Homework
from .serializers import (CourseSerializer, LessonSerializer, CommentSerializer,
                          RatingSerializer, HomeworkSerializer, EmailSerializer)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


class CourseViewSet(viewsets.ModelViewSet):
    ''' kurslar '''

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LessonViewSet(viewsets.ModelViewSet):
    ''' darslar va uyga vazifa joylash'''

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Search(APIView):
    ''' qidirish '''

    def get(self, request: Request):
        word = str(request.query_params.get('word'))
        lesson = Lesson.objects.filter(name__icontains=word)
        return Response({'lesson': LessonSerializer(lesson, many=True).data})

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    ''' darslarga izoh qoldirish '''

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RatingViewSet(viewsets.ModelViewSet):
    ''' darslarni baholash '''

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HomeworkViewSet(viewsets.ModelViewSet):
    ''' vazifalarni yuborish '''

    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EmailApi(APIView):
    ''' emailga xabar yuborish '''

    def get(self, request):
        email = EmailSerializer()
        return Response(email.data)

    def post(self, request: Request):
        email = EmailSerializer(data=request.data)
        email.is_valid()

        users = User.objects.all()
        for user in users:
            subject = email.validated_data.get('title')
            message = email.validated_data.get('text')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)

        return Response({'message': 'Yuborildi'})

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
