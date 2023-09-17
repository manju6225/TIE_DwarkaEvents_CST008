from django.contrib import admin
from database.models import connect

# Register your models here.


class connectadmin(admin.ModelAdmin):
    list_display = ("name", "city", "address", "event",
                    "pincode", "cc", "exp", "cvv")


admin.site.register(connect, connectadmin)
