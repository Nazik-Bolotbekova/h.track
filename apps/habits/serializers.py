from rest_framework import serializers

from apps.habits.models import Habit, MotivationPhrase

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        freq = data.get('habit_frequency')
        day_week = data.get('day_of_week')
        day_month = data.get('day_of_month')
        reminder = data.get('reminder_time')

        if freq == 'daily' and (day_week is not None or day_month is not None):
            raise serializers.ValidationError(
                'Для ежедневной привычки нельзя указывать день недели или день месяца.'
            )
        elif freq == 'weekly' and day_week is None:
            raise serializers.ValidationError('Укажите день недели')
        elif freq == 'monthly' and day_month is None:
            raise serializers.ValidationError('Укажите дату месяца')
        elif reminder is None:
            raise serializers.ValidationError('Укажите время напоминания')
        return data

class TrackingSerializer(serializers.Serializer):
    days_done = serializers.IntegerField()


class MotivationPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivationPhrase
        fields = '__all__'
