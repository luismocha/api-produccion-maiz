from django.http import JsonResponse
from django.shortcuts import render
from productoreslist_app.models import Productor

# Create your views here.
def proveeedor_list(request):
    productores=Productor.objects.all()
    data ={
        'productores':list(productores.values())
    }
    return JsonResponse(data)

