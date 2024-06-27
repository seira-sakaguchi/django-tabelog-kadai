from django.contrib import admin

from .models import CustomUser,StoreInfo,Category


class StoreInfoAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'category')
    search_fields = ('store_name',)



admin.site.register(CustomUser)
admin.site.register(StoreInfo,StoreInfoAdmin)
admin.site.register(Category)

