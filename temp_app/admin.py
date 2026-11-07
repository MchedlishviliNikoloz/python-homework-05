from django.contrib import admin
from temp_app.models import Book, Store, Author

# Register your models here.

admin.site.register(Store)
admin.site.register(Author)
admin.site.register(Book)