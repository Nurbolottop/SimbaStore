from django.contrib import admin

from apps.secondary import models

# Register your models here.
class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('subtitle', )
    list_display = ('subtitle', 'title')
    search_fields = ('subtitle', 'title')

################################################################################################################################################################################

class LookBookAddInline(admin.TabularInline):
    model = models.LookBookAdd
    fields = ('image',) # Add other fields if necessary

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        if obj:
            # Count how many images are already associated
            count = obj.look_book.count()
            # Adjust 'extra' to limit the total number of images to 4
            formset.extra = max(0, 4 - count)
        return formset


class LookBookFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [LookBookAddInline]

################################################################################################################################################################################

admin.site.register(models.Slide, SlideFilterAdmin)
admin.site.register(models.LookBook, LookBookFilterAdmin)
