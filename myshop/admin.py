from django.contrib import admin

from myshop.models import Book

class BookAdmin(admin.ModelAdmin):
    pass
#    list_display = ('address', 'city', 'state', 'zipcode', 'country', 'latitude', 'longitude')
#    fields = ['address', 'city', 'state', 'zipcode', 'country']

admin.site.register(Book, BookAdmin)

