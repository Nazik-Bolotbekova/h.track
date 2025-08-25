from django.db import models
from django.db.models import PositiveIntegerField

from apps.users.models import CustomUser
from apps.habits.choices import Frequency, Weekday


class Habit(models.Model):
    title = models.CharField(max_length=100,unique=True)
    description = models.TextField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    time_duration = models.PositiveIntegerField()
    is_done = models.BooleanField(default = True)
    completed_count = PositiveIntegerField(default=0)
    habit_frequency = models.CharField(max_length=50,choices=Frequency.choices)
    reminder_time = models.TimeField(null=True, blank=True)
    day_of_week = models.PositiveSmallIntegerField(choices=Weekday.choices,null=True,blank=True)
    day_of_month = models.PositiveSmallIntegerField(null=True,blank=True)
    last_reminded = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

class Tracker(models.Model):
    date = models.DateField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.habit)

    class Meta:
        verbose_name = 'Трекер'
        verbose_name_plural = 'Трекеры'

class MotivationPhrase(models.Model):
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Фраза'
        verbose_name_plural = 'Фразы'