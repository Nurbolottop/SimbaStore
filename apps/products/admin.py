from django.contrib import admin
from django.contrib.auth.models import User,Group

################################################################################################################################################################################

from apps.products import models 
# Register your models here.

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

class BrandFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

################################################################################################################################################################################

class TwoCategoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

################################################################################################################################################################################

class CollectionFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

################################################################################################################################################################################

class PriceFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

################################################################################################################################################################################

class SizeAdFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

################################################################################################################################################################################

class ColorAdFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

################################################################################################################################################################################

class ColorAdInline(admin.TabularInline):
    model = models.Color
    extra = 1  

class SizeAdInline(admin.TabularInline):
    model = models.Size
    extra = 1  

class ImageAdInline(admin.TabularInline):
    model = models.Image
    extra = 1  

class ProductFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [ColorAdInline,SizeAdInline,ImageAdInline]

################################################################################################################################################################################

class IndexImageInline(admin.TabularInline):
    model = models.IndexImage
    extra = 1  

class ColorAdIndexInline(admin.TabularInline):
    model = models.ColorIndex
    extra = 1  

class SizeAdIndexInline(admin.TabularInline):
    model = models.SizeIndex
    extra = 1  

class IndexProductFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [SizeAdIndexInline,ColorAdIndexInline,IndexImageInline]

################################################################################################################################################################################

admin.site.register(models.Category, CategoryFilterAdmin)
admin.site.register(models.Product, ProductFilterAdmin)
admin.site.register(models.Brand, BrandFilterAdmin)
admin.site.register(models.Collection, CollectionFilterAdmin)
admin.site.register(models.Price, PriceFilterAdmin)
admin.site.register(models.TwoCategory, TwoCategoryFilterAdmin)
admin.site.register(models.SizeAd, SizeAdFilterAdmin)
admin.site.register(models.ColorAd, ColorAdFilterAdmin)
admin.site.register(models.IndexProduct, IndexProductFilterAdmin)

################################################################################################################################################################################
