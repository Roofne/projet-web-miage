from django.contrib import admin

from .models import beneficiaire

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("Nom","prenom","postale","telephone")
admin.site.register(beneficiaire,ProfileAdmin)
