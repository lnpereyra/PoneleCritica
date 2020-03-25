from django.contrib import admin

# Register your models here.\

from .forms import RegModelForm
from .models import ParticipantesTorneo

class AdminParticipantesTorneo(admin.ModelAdmin):
    list_display = ["partnombre","partapellido","partpuntaje","partcat"]
    form = RegModelForm
    list_filter = ["partcat"]
    list_editable = ["partpuntaje"]
    search_fields = ["Apellido", "Nombre"]

admin.site.register(ParticipantesTorneo,AdminParticipantesTorneo)