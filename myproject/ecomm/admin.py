
from unicodedata import category
from django.contrib import admin

from .models import register_info, upload_product,Category,order
# Register your models here.


class register_dtls(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email']


admin.site.register(register_info, register_dtls)
admin.site.register(upload_product)
admin.site.register(Category)
admin.site.register(order)


