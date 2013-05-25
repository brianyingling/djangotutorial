from django.contrib import admin
from books.models import Publisher, Author, Book

# subclasses django.contrib.admin.ModelAdmin
# holds custom configuration for a specific admin model
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'email')
  search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'publisher', 'publication_date')
  # used to create a set of filters on the right side of the admin page
  list_filter = ('publication_date',)
  date_hierarchy = 'publication_date'
  ordering = ("-publication_date",)
  filter_horizontal = ('authors', )

admin.site.register(Publisher)

# register Author model with AuthorAdmin options
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
