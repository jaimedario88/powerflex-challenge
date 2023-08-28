from django.contrib import admin

from api.models import Factory, FactoryProductionRecord, Sprocket


class FactoryDataAdmin(admin.TabularInline):
    model = FactoryProductionRecord


class FactoryAdmin(admin.ModelAdmin):
    inlines = [
        FactoryDataAdmin,
    ]


admin.site.register(Sprocket, admin.ModelAdmin)
admin.site.register(Factory, FactoryAdmin)
