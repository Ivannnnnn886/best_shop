from django.contrib import admin
from .models import Category, Product, Gallery, Event, ContactInfo, Reservation
from django.utils.safestring import  mark_safe

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo_img_tag', 'price', 'category', 'is_visible', 'sort')
    list_display_links = ('id', 'name')
    list_editable = ('price', 'category', 'is_visible', 'sort')
    list_filter = ('is_visible', 'category')
    search_fields = ('name',)

    def photo_img_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ProductInline(admin.TabularInline):
    model = Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]


admin.site.register(Gallery)
admin.site.register(ContactInfo)
admin.site.register(Reservation)