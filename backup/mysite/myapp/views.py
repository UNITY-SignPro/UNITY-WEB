from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TranslateSerializer
from .models import Translate

class TranslateViewSet(viewsets.ModelViewSet) :
    queryset = Translate.objects.all()
    serializer_class = TranslateSerializer


# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Translate
# from .serializers import TranslateSerializer

# @api_view(['GET'])
# def get_api(request) :
#     queryset = Translate.objects.all()
#     serializer = TranslateSerializer(quertset)
#     return Response(serializer.data)
