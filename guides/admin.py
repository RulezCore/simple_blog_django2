from django.contrib import admin
from .models import Guide


# Register your models here.

class GuideAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Guide, GuideAdmin)
