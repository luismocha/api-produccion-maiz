from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        print(self)
        print('-----REQUEST')
        print(request)
        print(view)
        if request.method =='GET':
            return True 
        staff_permissio=bool(request.user and request.user.is_staff)
        print(staff_permissio)
        return staff_permissio
class CrearPostUserOrReadOnly():
    def has_object_permission(self,request,view,object):
        #safe== metodos get
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            ## el uusario que ha creado cualquier cosa en la aplicacion
            return object.post_creacion_user==request.user