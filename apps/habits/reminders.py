import os
import requests
from apps.habits.models import Habit
from django.utils import timezone
from dotenv import load_dotenv

load_dotenv()

bot = os.getenv('BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')


def send_telegram(chat_id: int, text: str):
    url =  f"https://api.telegram.org/bot{bot}/sendMessage"
    payload = {
        "chat_id" : chat_id,
        "text" : text
    }
    res = requests.post(url,data=payload)
    return res.json()


def should_remind(habit):
    if habit.reminder_time is None:
        return False

    now = timezone.localtime()
    habit_time = now.replace(
        hour=habit.reminder_time.hour,
        minute=habit.reminder_time.minute,
        second=0,
        microsecond=0
    )

    delta = abs((now - habit_time).total_seconds())

    if habit.habit_frequency == "daily":
        return delta < 60

    if habit.habit_frequency == "weekly":
        return now.weekday() == habit.day_of_week and delta < 60

    if habit.habit_frequency == "monthly":
        return now.day == habit.day_of_month and delta < 60

    return False


def check_all_habits():
    habits = Habit.objects.all()
    for habit in habits:
        if should_remind(habit):
            if not habit.last_reminded or (timezone.localtime() - habit.last_reminded).total_seconds() > 60:
                send_telegram(chat_id, f"Напоминание: {habit.title}")
                habit.last_reminded = timezone.localtime()
                habit.save(update_fields=['last_reminded'])



