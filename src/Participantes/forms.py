from django import forms

from .models import ParticipantesTorneo

class RegModelForm(forms.ModelForm):
    class Meta:
        model = ParticipantesTorneo
        fields = ["partnombre","partapellido","partcat"]

