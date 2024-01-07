from django.contrib import admin
from django.contrib.auth.models import User,Group

#My imports 
from apps.base import models 

# Register your models here.
class SettingsPhoneInline(admin.TabularInline):
    model = models.SettingsPhone
    extra = 1  


class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [SettingsPhoneInline]

################################################################################################################################################################################

admin.site.register(models.Settings, SettingsFilterAdmin)

################################################################################################################################################################################

admin.site.unregister(User)
admin.site.unregister(Group)