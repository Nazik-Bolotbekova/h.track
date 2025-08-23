from django.contrib import admin

from apps.habits.models import Habit, Tracker, MotivationPhrase

admin.site.register(MotivationPhrase)

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_filter = ('id','title')
    ordering = ('id',)

@admin.register(Tracker)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ('id','date','habit','user','is_done')
    list_display_links = ('id','user')
    search_fields = ('user',)
    list_filter = ('id','user')
    ordering = ('id',)

