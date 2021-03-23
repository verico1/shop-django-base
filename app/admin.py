from django.contrib import admin
from .models import call_us, note

admin.site.register(note)

@admin.register(call_us)
class call_usAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ('name', 'created_on')