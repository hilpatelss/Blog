from django.contrib import admin
from . import models
# Register your models here.
class Blog(admin.ModelAdmin):
    list_display=('b_img','b_title','b_heading','b_blog')
admin.site.register(models.Blog ,Blog)