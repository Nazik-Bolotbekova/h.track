from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.habits.views import HabitViewSet, TrackingProgress, MotivationPhraseViewSet, TestAPI, Test2API

router = DefaultRouter()
router.register('habits',HabitViewSet)
router.register('motivation',MotivationPhraseViewSet)

urlpatterns = [

    path('get_progress/',TrackingProgress.as_view(),name='get_progress'),
    path('test/',TestAPI.as_view(),name='test'),
    path('test2/',Test2API.as_view(),name='test2'),
    *router.urls,
]
