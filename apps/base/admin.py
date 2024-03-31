from django.contrib import admin

from apps.base.models import Entidade


@admin.register(Entidade)
class EntidadeAdmin(admin.ModelAdmin):
    ...
