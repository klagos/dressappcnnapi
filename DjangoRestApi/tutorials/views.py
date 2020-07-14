from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import Tutorial, Image
from tutorials.serializers import TutorialSerializer, ImageSerializer
from rest_framework.decorators import api_view

import wget
import os

@api_view(['GET', 'POST', 'DELETE'])
def image_list(request):
    if request.method == 'GET':
        images = Image.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            images = images.filter(title__icontains=title)
        
        images_serializer = ImageSerializer(images, many=True)
        return JsonResponse(images_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        image_data = JSONParser().parse(request)
        image_url = image_data['url']
        local_image_filename = wget.download(image_url)
        # Poner codigo de la CNN aqui
        tipo = "blusa"
        color = "rojo"
        usuario = 1
        image_data = {"usuario": 1, "tipo": tipo, "color": color}
        image_serializer = ImageSerializer(data=image_data)
        os.remove(local_image_filename) 
        if image_serializer.is_valid():
            image_serializer.save()
            return JsonResponse(image_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = image.objects.all().delete()
        return JsonResponse({'message': '{} images were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        image_url = tutorial_data['url']
        local_image_filename = wget.download(image_url)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        os.remove(local_image_filename) 
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    
