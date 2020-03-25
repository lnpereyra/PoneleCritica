from django.shortcuts import render

from .models import ParticipantesTorneo 

# Create your views here.
def participantes_view(request):
    obj = ParticipantesTorneo.objects.get(id=1)
    context = {
        "nombre": obj.partnombre,
        "apellido": obj.partapellido,
        "puntaje": obj.partpuntaje,
        "categoria": obj.partcat,
        "fechasjug": obj.partjugadas,
    }

    return render(request, "test.html" , context)