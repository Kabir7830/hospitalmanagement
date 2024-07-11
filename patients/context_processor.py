from . models import *


def GlobalData(request):
    
    doctors = Doctors.objects.all()
    
    return {"doctors":doctors}