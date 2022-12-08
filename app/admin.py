from django.contrib import admin

# Register your models here.
#registrar el modelo en la aplicacion 
from app.models import Canton, Parroquia, Productor
# Register your models here.
admin.site.register(Canton)
admin.site.register(Parroquia)
admin.site.register(Productor)