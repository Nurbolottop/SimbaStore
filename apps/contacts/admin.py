from django.contrib import admin

################################################################################################################################################################################

from apps.contacts import models 

# Register your models here.
class ReviewFilterAdmin(admin.ModelAdmin):
    list_filter = ("title", "message" )
    list_display = ("title", "message" )
    search_fields = ("title", "message" )

################################################################################################################################################################################

class SubscriberFilterAdmin(admin.ModelAdmin):
    list_filter = ('email', )
    list_display = ('email', 'subscribed_at')
    search_fields = ('email', 'subscribed_at')
    
################################################################################################################################################################################

class NewsletterFilterAdmin(admin.ModelAdmin):
    list_filter = ('subject', )
    list_display = ('subject', 'message')
    search_fields = ('subject', 'message')

################################################################################################################################################################################

admin.site.register(models.Review,ReviewFilterAdmin)
admin.site.register(models.Newsletter, NewsletterFilterAdmin)
admin.site.register(models.Subscriber, SubscriberFilterAdmin)