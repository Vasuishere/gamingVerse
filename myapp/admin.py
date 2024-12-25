from django.contrib import admin
from .models import Header,Tournament,Winner,User,game


# Register your models here.
admin.site.register(Header)
admin.site.register(Tournament)
admin.site.register(Winner)
admin.site.register(User)
admin.site.register(game)
