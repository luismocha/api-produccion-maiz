from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method =='GET':
            return True 
        staff_permissio=bool(request.user and request.user.is_staff)
        
        return staff_permissio
class AdminAuthPutOrReadOnly(permissions.IsAdminUser):
     def has_permission(self, request, view):
        staff_permissio=bool(request.user and request.user.is_staff)
        return staff_permissio
        #if request.method =='GET' or request.method =='PUT' or request.method =='DELETE':
   
class AuthPermisos(permissions.BasePermission):
    def has_object_permission(self,request,view,object):
        #safe== metodos get
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            ## el uusario que ha creado cualquier cosa en la aplicacion
            return object.user==request.user