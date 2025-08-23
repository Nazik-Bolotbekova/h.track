from django.contrib import admin

from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email')
    list_filter = ('id','first_name')
    list_display_links = ('first_name','email')
    search_fields = ('id','first_name')
    ordering = ('id',)
