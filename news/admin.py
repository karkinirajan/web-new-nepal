from django.contrib import admin

from .models import (
    Blog,
    Business,
    Contact,
    Covid,
    Education,
    Entertainment,
    Health,
    International,
    LifeStyle,
    Literature,
    National,
    Newsletter,
    Politics,
    Post,
    Sports,
    Tech,
    Youtube,
)

admin.site.register(Post)
admin.site.register(National)
admin.site.register(International)
admin.site.register(Covid)
admin.site.register(Sports)
admin.site.register(Politics)
admin.site.register(Entertainment)
admin.site.register(LifeStyle)
admin.site.register(Literature)
admin.site.register(Blog)
admin.site.register(Tech)
admin.site.register(Health)
admin.site.register(Business)
admin.site.register(Education)
admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Youtube)

# admin.site.register(Comment)
