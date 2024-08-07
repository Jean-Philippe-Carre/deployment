from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import json
from .models import Post
from .serializers import PostSerializer

# Create your views here.

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class PostView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        data = Post.objects.all()
        serialiser = PostSerializer(data, many=True)
        return Response(serialiser.data)

    def post(self, request, *args, **kwargs):
        serialiser = PostSerializer(data=request.data)  # serialise the data
        if serialiser.is_valid():  # check if the serialised data is valid
            serialiser.save()  # save the serialised data
            # return the serialised data with status code 201
            return Response(serialiser.data)
        # return the errors with status code 400
        return Response(serialiser.errors)

    def delete(self, request, id, *args, **kwarg):
        article = Post.objects.get(pk=id)
        article.delete()
        return Response({"Status": "Done"}, status=204)

    def put(self, request, *args, **kwargs):
        data = request.data
        original = Post.objects.get(id=data['id'])
        if 'title' in data:
            original.title = data['title']
        if 'content' in data:
            original.content = data['content']
        original.save()

        return Response({'Status': 'Updated'}, status=400)

# @csrf_exempt
# def view_posts(request):
#     if request.method == 'GET':
#         data = Post.objects.all()
#         serialiser = PostSerializer(data, many=True)
#         return JsonResponse(serialiser.data, safe=False)


# @csrf_exempt
# def view_post_by_id(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)  # parse the request body json
#         id = data['id']  # extract the id from the json
#         data = Post.objects.get(id=id)  # get the post object with the id
#         serialiser = PostSerializer(data)  # serialise the post object
#         # return the serialised data
#         return JsonResponse(serialiser.data, safe=False)


# @csrf_exempt
# def create_post(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)  # parse the request body json
#         serialiser = PostSerializer(data=data)  # serialise the data
#         if serialiser.is_valid():  # check if the serialised data is valid
#             serialiser.save()  # save the serialised data
#             # return the serialised data with status code 201
#             return JsonResponse(serialiser.data, status=201)
#         # return the errors with status code 400
#         return JsonResponse(serialiser.errors, status=400)
