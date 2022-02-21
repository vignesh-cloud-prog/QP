from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import *

# Create your views here.
def create_eduation_type(request):
    if request.is_ajax and request.method == "POST":
        try:
            # print(request.POST)
            name = request.POST.get('name')
            paper_type = request.POST.get('paper_type')

            instance =ExaminationType.objects.create(
                name = name,
                paper_type = paper_type,
                )
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

def create_governing_body(request):
    if request.is_ajax and request.method == "POST":
        try:
            print(request.POST)
            name = request.POST.get('name')
            education = request.POST.get('education')

            instance = GoverningBody.objects.create(
                name = name,
                
                )
            instance.save()
            education_ins=ExaminationType.objects.get(id=education)
            instance.education.add(education_ins)
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=400)