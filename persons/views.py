from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from persons.models import PersonsModel
from persons.serializers.PersonsSerializer import ListPersonsSerializer, PersonsSerializer, UpdatePersonSerializer, DeletePersonSerializer
from django.http import HttpResponse

# Create your views here.
class PersonsAPPView(APIView):   
    """ Creacion de personas """
    def post(self, request):
        response = dict()
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}
            
        serializer = PersonsSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            person = serializer.create(serializer.data)
            serializer_data = ListPersonsSerializer(person, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)     
    
    """ Consulta de personas registradas
        Se puede listar todos los registros o se puede filtrar la consulta 
        por los campos en la tabla
    """
    def get(self, request):
        response = dict()
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}
            
        queryset = PersonsModel.objects.filter(**data).order_by('id')
        serializer = ListPersonsSerializer(queryset, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)
    
    """ Modificar datos de una persona registrada """
    def patch(self, request):
        response = dict()
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}       
        
        try:
            serializer = UpdatePersonSerializer(data=data)
            """ Se valida si no hay errores la operacion de modificar. Si hay errores, se retorna """
            if serializer.is_valid(raise_exception=False):
                """ Se verifica si existe la persona """
                queryset = PersonsModel.objects.get(id=data["id"])    
                person = serializer.update(queryset, data)
                serializer_data = ListPersonsSerializer(person)            
                response["data"] = serializer_data.data
                return JsonResponse(status=status.HTTP_200_OK, data=response)
            else:
                response["errors"] = serializer.errors
                return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response) 
        except PersonsModel.DoesNotExist:
            response["errors"] = "Person not found"
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)
    
    """ Modificar datos de una persona registrada """
    def delete(self, request):
        response = dict()
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}
        
        try:
            serializer = DeletePersonSerializer(data=data)            
            """ Se valida si no hay errores la operacion de eliminar. Si hay errores, se retorna """
            if serializer.is_valid(raise_exception=False):
                """ Se verifica si existe la persona """
                queryset = PersonsModel.objects.get(id=data["id"])    
                serializer.delete(queryset)       
                response["data"] = {}
                return JsonResponse(status=status.HTTP_200_OK, data=response)
            else:
                response["errors"] = serializer.errors
                return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response) 
        except PersonsModel.DoesNotExist:
            response["errors"] = "Person not found"
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response) 
    
    