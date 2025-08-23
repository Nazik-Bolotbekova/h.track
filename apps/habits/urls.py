from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.habits.views import HabitViewSet, TrackingProgress, MotivationPhraseViewSet

router = DefaultRouter()
router.register('habits',HabitViewSet)
router.register('motivation',MotivationPhraseViewSet)

urlpatterns = [

    path('get_progress/',TrackingProgress.as_view(),name='get_progress'),
    *router.urls,
]
