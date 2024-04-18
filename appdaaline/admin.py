from django.contrib import admin
from .models import CoisaParaFazer, Lugar
# Register your models here.

class CoisaAdmin(admin.ModelAdmin):
  list_display = ['nome', 'icone', 'numero', 'descricao', 'tempo', 'energia']
  ordering = ['numero']
  
admin.site.register(CoisaParaFazer, CoisaAdmin)

class LugarAdmin(admin.ModelAdmin):
  list_display = ['nome', 'link', 'atividade', 'endereco', 'custo']
  ordering = ['nome']

admin.site.register(Lugar, LugarAdmin)


