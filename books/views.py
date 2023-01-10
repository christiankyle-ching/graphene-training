from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from books.models import Author
from books.serializers import AuthorSerializer

# Create your views here.


@csrf_exempt
def author_list(request):

    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=True)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=True)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def author_detail(request, pk):

    # Get author object first
    try:
        author = Author.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    # Get details
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data)

    # Update details
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(author, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    # Delete
    elif request.method == 'DELETE':
        author.delete()
    return HttpResponse(status=204)
