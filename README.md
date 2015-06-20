Photography Website

This is a basic photography based website with a django backbone. 

uploading images to the site is done via the Django admin panel. When uploading images, the images will take a Name, Tag, and Album filed. These fileds are stored in the sqllite database to later call upon the images. Upon uploading, Django will create two additional images of different sizes for use as thumbnames.

The front end of the website is build off of Boostrap. (still under consturction) 

Each gallery page will take the album name to fetch the images from teh database for display on the page. 

The home page takes a random sample of images either from a specific database or from all databases ( can be configured) and displayes that random set to the home page. 
