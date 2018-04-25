# Register your models here.
from modelo.bolsa.models import PlanoDeContas
from django.contrib import admin


class PlanoDeContasAdmin(admin.ModelAdmin):
    list_display = ['classification', 'name', 'reduced_account', 'sn', 'n', 'source', 'account_type']
    search_fields = ['classification', 'name', 'reduced_account', 'sn', 'n', 'source', 'account_type']


admin.site.register(PlanoDeContas, PlanoDeContasAdmin)
