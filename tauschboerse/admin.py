from django.contrib import admin
from tauschboerse.models import Gegenstand

# Register your models here.
class GegenstandAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_draft')
    pass
admin.site.register(Gegenstand, GegenstandAdmin)
