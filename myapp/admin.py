from django.contrib import admin

from .models import Genre, Artist, Album, News, Review, UserMessage

# Register your models here.
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(News)
admin.site.register(UserMessage)
admin.site.register(Review)