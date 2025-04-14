from django.contrib import admin

from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'age')
    search_fields = ('user__username', 'bio', 'location')
    list_filter = ('age',)
    ordering = ('user',)
    list_per_page = 10
    list_display_links = ('user',)
    fieldsets = (
        (None, {
            'fields': ('user', 'bio', 'location', 'age')
        }),
    ) 