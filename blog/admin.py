from django.contrib import admin
from .models import Manclothes, Wclothes, Banner, Devices, Laptops, Mbanner, Wbanner, Contact, Aboutus

# Register your models here.

admin.site.register(Manclothes)
admin.site.register(Wclothes)
admin.site.register(Banner)
admin.site.register(Devices)
@admin.register(Laptops)
class LaptopsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
admin.site.register(Mbanner)
admin.site.register(Wbanner)
admin.site.register(Contact)
admin.site.register(Aboutus)









