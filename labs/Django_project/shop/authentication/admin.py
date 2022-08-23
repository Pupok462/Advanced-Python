from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city')
    list_display_links = ('user', 'city')


admin.site.register(UserProfile, UserProfileAdmin)
