from django.contrib import admin

# Register your models here.
#registrar el modelo en la aplicacion 
from app.models import Canton, Intermediario, Parroquia, Produccion, Productor, Tipo_Productor
# Register your models here.
admin.site.register(Canton)
admin.site.register(Parroquia)
admin.site.register(Productor)
admin.site.register(Tipo_Productor)
admin.site.register(Produccion)
admin.site.register(Intermediario)