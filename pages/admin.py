from django.contrib import admin
from .models import Pages


# Register your models here.

class PagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'created')


admin.site.register(Pages, PagesAdmin)
