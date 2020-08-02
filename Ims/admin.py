
from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import Device,Desktop,Mobile,Laptop


admin.site.register(Laptop)
admin.site.register(Mobile)
admin.site.register(Desktop)

# class ViewAdmin(ImportExportModelAdmin):

