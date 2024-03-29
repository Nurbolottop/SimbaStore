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

class BannerAddInline(admin.TabularInline):
    model = models.BannerAdd
    def get_max_num(self, request, obj=None, **kwargs):
        if obj:
            # Вы можете настроить количество доступных форм здесь
            max_num = 6 - obj.look_book.count()
            return max_num
        return 6


class BannerFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    list_display = ('image', )
    search_fields = ('image', )
    inlines = [BannerAddInline]

################################################################################################################################################################################

class FaqsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'message')
    search_fields = ('title', 'message')

################################################################################################################################################################################

class TeamFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'work')
    search_fields = ('title', 'work')

################################################################################################################################################################################

admin.site.register(models.Slide, SlideFilterAdmin)
admin.site.register(models.LookBook, LookBookFilterAdmin)
admin.site.register(models.Banner, BannerFilterAdmin)
admin.site.register(models.Faqs, FaqsFilterAdmin)
admin.site.register(models.Team, TeamFilterAdmin)

