from django.http import JsonResponse
from django.shortcuts import render
from app.models import Canton
# Create your views here.
class ListarCantones():
    data={
        'probando':'gffgjhgh'
    }
    return JsonResponse(data)