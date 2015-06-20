from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import os
from PIL import Image as PImage
from mwalkerphotos.settings import MEDIA_ROOT
from string import join

from tempfile import *
from django.core.files import File
# Create your models here.

def only_filename(instance, filename):
    return filename


class Album(models.Model):
    title =  models.CharField(max_length=120)
    public = models.BooleanField(default=True)
    def __unicode__(self):
        return self.title
        
        
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag
        
class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=False)
    image = models.FileField(upload_to=only_filename)
    tags = models.ManyToManyField(Tag, blank=True)
    albums = models.ManyToManyField(Album, blank=False)
    size = models.CharField(max_length=120, blank=True, null=False)
    
    
    thumbnail2 = models.ImageField(upload_to=only_filename, blank=True, null=True)
    thumbnail3 = models.ImageField(upload_to=only_filename, blank=True, null=True)
    
    def thumb_print(self):
        path, file = os.split(self.thumbnail2)
        return file
   


    
    def save(self, *args, **kwargs):
        """Save Image Dimensions. """
        super(Image, self).save(*args, **kwargs)
        im = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
        self.width, self.height = im.size
        
        # large thumbnail
        fn, ext = os.path.splitext(self.image.name)
        im.thumbnail((336,280), PImage.ANTIALIAS)
        thumb_fn = fn + "-336x280" + ext
        tf2 = NamedTemporaryFile()
        im.save(tf2.name, "JPEG")
        self.thumbnail2.save(thumb_fn, File(open(tf2.name)), save=False)
        tf2.close()

       # small thumbnail
#        im.thumbnail((40,40), PImage.ANTIALIAS)
#        thumb_fn = fn + "-thumb" + ext
#        tf = NamedTemporaryFile()
#        im.save(tf.name, "JPEG")
#        self.thumbnail.save(thumb_fn, File(open(tf.name)), save=False)
#        tf.close()
        fn, ext = os.path.splitext(self.image.name)
        im.thumbnail((300,250), PImage.ANTIALIAS)
        thumb_fn = fn + "-300x250" + ext
        tf = NamedTemporaryFile()
        im.save(tf.name, "JPEG")
        self.thumbnail3.save(thumb_fn, File(open(tf.name)), save=False)
        tf.close()
        
        
        
        super(Image, self).save(*args, **kwargs)
        
    def size(self):
        """image size"""
        im = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
        width, height = im.size
        return '%s x %s' % (width, height)
    
    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(join(lst, ','))
        
    def albums_(self):
        lst = [x[1] for x in self.albums.values_list()]
        return str(join(lst, ','))
        
    def thumbnail(self):
        path, filename = os.path.split(self.image.name)
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % ((self.thumbnail2.name, self.thumbnail2.name))


    thumbnail.allow_tags = True
    
    def __unicode__(self):
        path, filename = os.path.split(self.image.name)
        return filename


    

