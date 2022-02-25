from django.contrib import admin

from .models import ComunityMessages

# Register your models here.


class AdminComunityMessages(admin.ModelAdmin):
    """ Dummy Tag """

    readonly_fields = ('date', 'like')

    fields = ('username', 'title', 'message_content', 'date',
              'like')

    list_display = ('username', 'title', 'like')

admin.site.register(ComunityMessages, AdminComunityMessages)
