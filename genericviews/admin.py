from django.contrib import admin
from .models import Book
from django.utils.safestring import mark_safe

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'publisher','image_tag']

    def image_tag(self, obj):
        if obj.image:
            return mark_safe('<img src="%s%s" width="150" height="150" />')
        else:
            return 'No Image'
    image_tag.short_description = 'Image'

admin.site.register(Book, BookAdmin)
admin.site.site_header = "Mening Admin Panelim"
