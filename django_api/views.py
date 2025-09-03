from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=subcategory_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)

    #validating for already existing data
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This item already exists')
    
    if item.is_valid():
        item.save()
        return Response(item.data, status=201)
    else:
        return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)

