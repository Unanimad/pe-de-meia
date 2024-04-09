from django.contrib import admin

from .models import Incentivo, TipoCiclo, Ciclo, InconsistenciaCiclo


@admin.register(Incentivo)
class IncentivoAdmin(admin.ModelAdmin):
    ...


@admin.register(TipoCiclo)
class TipoCicloAdmin(admin.ModelAdmin):
    ...


@admin.register(Ciclo)
class CicloAdmin(admin.ModelAdmin):
    ...


@admin.register(InconsistenciaCiclo)
class InconsistenciaCicloAdmin(admin.ModelAdmin):
    ...
