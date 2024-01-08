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

class SaleFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

################################################################################################################################################################################

class BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

################################################################################################################################################################################

class DevizAddInline(admin.TabularInline):
    model = models.DevizAdd
    def get_max_num(self, request, obj=None, **kwargs):
        if obj:
            max_num = 3 - obj.deviiz.count()
            return max_num
        return 3


class DevizFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
    inlines = [DevizAddInline]

################################################################################################################################################################################

admin.site.register(models.Settings, SettingsFilterAdmin)
admin.site.register(models.Category, CategoryFilterAdmin)
admin.site.register(models.Sale, SaleFilterAdmin)
admin.site.register(models.Blog, BlogFilterAdmin)
admin.site.register(models.Devis, DevizFilterAdmin)

################################################################################################################################################################################

admin.site.unregister(User)
admin.site.unregister(Group)