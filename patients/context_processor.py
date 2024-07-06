from . models import *


def GlobalData():
    
    doctors = Doctors.objects.all()
    
    return {"doctors":doctors}