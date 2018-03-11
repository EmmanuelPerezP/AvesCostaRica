from django.contrib import admin
from .models import Ave, Clase, Especie, Familia, Genero, Orden, Suborden, Image


class ImageInline(admin.TabularInline):
    model = Image   # related model
    extra = 1  # number of new record fields


class AveAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Ave, AveAdmin)
admin.site.site_title = 'Aves Costa Rica'
admin.site.site_header = 'Administracion de Aves'
admin.site.register(Clase)
admin.site.register(Especie)
admin.site.register(Familia)
admin.site.register(Genero)
admin.site.register(Orden)
admin.site.register(Suborden)
admin.site.register(Image)
