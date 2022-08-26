from django.contrib import admin
from .models import Salle, SalleAdmin
admin.site.register(Salle, SalleAdmin)

# from .models import *

# admin.site.register(Eleve)
# admin.site.register(Cours)
# admin.site.register(Point)
# Register your models here.
