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
    def get_max_num(self, request, obj=None, **kwargs):
        if obj:
            # Вы можете настроить количество доступных форм здесь
            max_num = 4 - obj.look_book.count()
            return max_num
        return 4


class LookBookFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [LookBookAddInline]

################################################################################################################################################################################

admin.site.register(models.Slide, SlideFilterAdmin)
admin.site.register(models.LookBook, LookBookFilterAdmin)
