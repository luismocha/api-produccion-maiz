from django.urls import path
from productoreslist_app.views import proveeedor_list
urlpatterns = [
    path('list/',proveeedor_list,name='productores-list')
]
