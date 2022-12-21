from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import listar_usuarios_view, registration_view,logout_view
urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register/',registration_view,name='registro'),
    path('logout/',logout_view,name='logout'),
    path('users',listar_usuarios_view,name='list-user'),
]
