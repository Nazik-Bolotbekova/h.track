from django.db import models

class Frequency(models.TextChoices):
    DAILY = "daily", "Daily"
    WEEKLY = "weekly", "Weekly"
    MONTHLY = "monthly", "Monthly"

class Weekday(models.IntegerChoices):
    MON = 0, "Monday"
    TUE = 1, "Tuesday"
    WED = 2, "Wednesday"
    THU = 3, "Thursday"
    FRI = 4, "Friday"
    SAT = 5, "Saturday"
    SUN = 6, "Sunday"
