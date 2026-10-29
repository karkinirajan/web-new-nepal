from django.contrib import admin

from .models import Comment, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Comment)
