from django.contrib import admin
from reversion.admin import VersionAdmin
from catalogue.models import Book, Author, Publisher

class BookAdmin(VersionAdmin):
    list_display = ('title', 'publisher', 'isbn', 'year', 'status',)
    list_filters = ('title', 'publisher', 'year',)
    search_fields = ('title', 'publisher', 'isbn')
    
class AuthorAdmin(VersionAdmin):
    list_display = ('name', 'email',)
    search_fields = ('name', 'email',)
    
class PublisherAdmin(VersionAdmin):
    list_display = ('name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
