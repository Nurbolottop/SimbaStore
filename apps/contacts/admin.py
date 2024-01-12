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

class ContactFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'message')
    search_fields = ('name', 'message')

################################################################################################################################################################################

class BuyFilterAdmin(admin.ModelAdmin):
    list_filter = ('username', )
    list_display = ('username', 'product')
    search_fields = ('username', 'product')

################################################################################################################################################################################

admin.site.register(models.Review,ReviewFilterAdmin)
admin.site.register(models.Newsletter, NewsletterFilterAdmin)
admin.site.register(models.Subscriber, SubscriberFilterAdmin)
admin.site.register(models.Contact, ContactFilterAdmin)
admin.site.register(models.Buy, BuyFilterAdmin)
