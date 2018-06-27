from django.contrib import admin

# Register your models here.
from chat.models import Message


class MessageAdmin(admin.ModelAdmin):  # изучить поля как будет время
    list_display = ['author', 'text']
    search_fields = ['author__username', 'text']


admin.site.register(Message, MessageAdmin)
