from django.contrib import admin

# Register your models here.\

from .forms import RegModelForm
from .models import ParticipantesTorneo

class AdminParticipantesTorneo(admin.ModelAdmin):
    list_display = ["partnombre","partapellido","partcat"]
    form = RegModelForm
    list_filter = ["partcat"]
    search_fields = ["Apellido", "Nombre"]

admin.site.register(ParticipantesTorneo,AdminParticipantesTorneo)