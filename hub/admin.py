from django.contrib import admin
from .models import Post
# To add our posts here we import the data
admin.site.register(Post)
# Now we can see the post Data and choose to delete it or not
