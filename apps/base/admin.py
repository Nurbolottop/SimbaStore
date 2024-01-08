from django.contrib import admin
from django.contrib.auth.models import User,Group

################################################################################################################################################################################

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

class CategoryAddInline(admin.TabularInline):
    model = models.CategoryAdd
    def get_max_num(self, request, obj=None, **kwargs):
        if obj:
            max_num = 5 - obj.categorys.count()
            return max_num
        return 5


class CategoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [CategoryAddInline]

################################################################################################################################################################################

admin.site.register(models.Settings, SettingsFilterAdmin)
admin.site.register(models.Category, CategoryFilterAdmin)


################################################################################################################################################################################

admin.site.unregister(User)
admin.site.unregister(Group)