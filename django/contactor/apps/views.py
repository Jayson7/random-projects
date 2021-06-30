from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import ContactSerializer 
from rest_framework import viewsets, status
from .models import Contact                 
from rest_framework.decorators import api_view
from rest_framework.response import Response
class ContactView(viewsets.ModelViewSet):  
    serializer_class = ContactSerializer   
    queryset = Contact.objects.all()     
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

@api_view(['GET','POST', 'PUT', 'DELETE'])
def contacthome(request):
    contact = Contact.objects.all()
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)




@api_view(['GET','POST', 'PUT', 'DELETE'])
def contactdetail(request, pk):
    contact = Contact.objects.get(pk=pk)
    serializer = ContactSerializer(contact, many=False)
    return Response(serializer.data)



@api_view(['GET','POST', 'PUT', 'DELETE'])
@parser_classes([JSONParser])
def contactCreate(request, format=None):
    # contact = Contact.objects.all()
    serializer = ContactSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','POST', 'PUT', 'DELETE'])
def contactUpdate(request,pk, format=None):
    contact = Contact.objects.get(id=pk)
   
    serializer = ContactSerializer(instance=contact, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.data)


@api_view(['GET','POST', 'PUT', 'DELETE'])
def contactDelete(request,pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return Response("Deleted")
