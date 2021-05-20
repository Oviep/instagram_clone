from django.contrib import admin

# Register your models here.
import photo_app
from photo_app.models import Post

admin.site.register(Post)