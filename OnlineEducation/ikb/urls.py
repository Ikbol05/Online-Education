from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CourseViewSet, LessonViewSet, CommentViewSet, RatingViewSet, HomeworkViewSet, Search, EmailApi)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()

router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('comments', CommentViewSet)
router.register('ratings', RatingViewSet)
router.register('homework', HomeworkViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


'''

/api/v1/courses/ - Kurslarni ro'yxati va yaratish

/api/v1/courses/pk/ - Kursni ko'rish, yangilash va o'chirish

/api/v1/lessons/ - Darslarni ro'yxati va yaratish

/api/v1/lessons/pk/ - Darsni ko'rish, yangilash va o'chirish

/api/v1/comments/ - Izohlarni ro'yxati va yaratish

/api/v1/comments/pk/ - Izohni ko'rish, yangilash va o'chirish

/api/v1/ratings/ - Baholarni ro'yxati va yaratish

/api/v1/ratings/pk/ - Bahoni ko'rish, yangilash va o'chirish

/api/v1/vazifa/ - Vazifa topshirish

/api/v1/vazifa/pk/ - Vazifa topshirish va o'chirish


'''

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('email-send/', EmailApi.as_view()),

    path('api-auth/', include('rest_framework.urls')),

    path('search/', Search.as_view()),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
