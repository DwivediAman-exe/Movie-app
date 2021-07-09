from django.contrib import admin
from .models import *
# Register your models here.


class MyMovie(admin.ModelAdmin):
    list_display = ('name', 'description', 'year', 'start', 'show')
    list_filter = ('start', 'show')


admin.site.register(Movie, MyMovie)
