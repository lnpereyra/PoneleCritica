from django.shortcuts import render

from .models import ParticipantesTorneo 

# Create your views here.
def participantes_view(request):
    # obj = ParticipantesTorneo.objects.all().order_by('puntaje')
    # context = {
    #     "nombre": obj.partnombre,
    #     "apellido": obj.partapellido,
    #     "puntaje": obj.partpuntaje,
    #     "categoria": obj.partcat,
    #     "fechasjug": obj.partjugadas,
    # }
    queryset = ParticipantesTorneo.objects.all().order_by('-partpuntaje')
    context = {
        "queryset": queryset,
    }

    return render(request, "test.html" , context)

def participantes_list(request):
    queryset = ParticipantesTorneo.objects.all().order_by('partnombre')
    context = {
        "queryset": queryset,
    }

    return render(request,'participantes.html',context)