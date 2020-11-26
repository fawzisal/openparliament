from django.contrib import admin

from parliament.alerts.models import *

class PoliticianAlertAdmin(admin.ModelAdmin):

    list_display = ('email', 'politician', 'active', 'created')
    search_fields = ('email', 'politician__name')

admin.site.register(PoliticianAlert, PoliticianAlertAdmin)


class TopicAdmin(admin.ModelAdmin):

    list_display = ['query', 'created', 'last_found']
    search_fields = ['query']
    ordering = ['-created']


class SubscriptionAdmin(admin.ModelAdmin):

    list_display = ['user', 'topic', 'active', 'created', 'last_sent']
    search_fields = ['user__email']
    list_filter = ['active', 'created', 'last_sent']
    ordering = ['-created']

admin.site.register(Topic, TopicAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(SeenItem)