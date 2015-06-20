from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from models import Album, Tag, Image
# Register your models here.






class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title"]
    
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]
    
class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["__unicode__", "title", "size", "tags_", "albums_", "thumbnail"]
    list_filter =["tags", "albums"]
    
    
    
    
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)