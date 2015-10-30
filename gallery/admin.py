from django.contrib import admin
from .models import Item, Photo

# Register your models here.
class PhotoInline(admin.StackedInline):
    model = Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption', 'item')


class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('name','description')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Item, ItemAdmin)
