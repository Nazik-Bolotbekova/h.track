from celery import shared_task
import os
from django.utils import timezone
from apps.habits.models import Habit
from dotenv import load_dotenv
from apps.habits.reminders import send_telegram, should_remind

import requests
try:
    print(requests.get("https://api.telegram.org").status_code)
except Exception as e:
    print("TG REQUEST FAILED:", e)


load_dotenv()

chat_id = os.getenv('TELEGRAM_CHAT_ID')

@shared_task
def check_all_habits(now=None):
    if now is None:
        now = timezone.localtime()

    habits = Habit.objects.all()
    for habit in habits:
        if should_remind(habit):
            if not habit.last_reminded or (timezone.localtime() - habit.last_reminded).total_seconds() > 60:
                send_telegram(chat_id, f"Напоминание: {habit.title}")
                habit.last_reminded = timezone.localtime()
                habit.save(update_fields=['last_reminded'])



