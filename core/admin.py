from django.contrib import admin
from .models import Feriado, Aula, Sala, Professor, Turma, Curso, Turno

class FeriadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'ponto_facultativo')
    list_filter = ('ponto_facultativo',)

class AulaAdmin(admin.ModelAdmin):
    list_display = ('professor', 'data', 'status', 'sala', 'turma')
    list_filter = ('status', 'data', 'turma')

admin.site.register(Feriado, FeriadoAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Sala)
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Curso)
admin.site.register(Turno)
