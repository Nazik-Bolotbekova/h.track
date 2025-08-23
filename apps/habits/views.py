from random import randint

from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from apps.habits.models import Habit, Tracker, MotivationPhrase
from apps.habits.serializers import HabitSerializer, TrackingSerializer, MotivationPhraseSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TrackingProgress(generics.GenericAPIView):
    serializer_class = TrackingSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses=TrackingSerializer,
    )
    def get(self, request):
        days_done = (
            Tracker.objects
                   .filter(is_done=True)
                   .values('date')
                   .distinct()
                   .count()
        )
        serializer = self.get_serializer({'days_done': days_done})
        return Response(serializer.data)


class MotivationPhraseViewSet(ReadOnlyModelViewSet):
    queryset = MotivationPhrase.objects.all()
    serializer_class = MotivationPhraseSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False)
    def random(self, request):
        count = MotivationPhrase.objects.count()
        if count > 0:
            idx = randint(0, count - 1)
            quote = MotivationPhrase.objects.all()[idx]
            serializer = MotivationPhraseSerializer(quote)
            return Response(serializer.data,status=200)
        return Response({"detail": "No phrases found"}, status=404)




