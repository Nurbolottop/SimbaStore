from django.contrib import admin

from apps.secondary import models

# Register your models here.
class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('subtitle', )
    list_display = ('subtitle', 'title')
    search_fields = ('subtitle', 'title')

################################################################################################################################################################################

admin.site.register(models.Slide, SlideFilterAdmin)