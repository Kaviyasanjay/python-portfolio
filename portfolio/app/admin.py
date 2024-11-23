from django.contrib import admin
from .models import SectionContent


admin.site.site_header = "KAVIYA SANKAR"
admin.site.site_title = "KAVIYA PORTFOLIO"
admin.site.index_title = "Welcome to the Admin Panel"

@admin.register(SectionContent)
class SectionContentAdmin(admin.ModelAdmin):
    list_display = ('section', 'title', 'image')
