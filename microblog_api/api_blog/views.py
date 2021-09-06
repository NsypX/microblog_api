from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Post
from .serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_opps(request):
    if request.method == 'GET':
        posts = Post.objects.order_by('-date','likes')
        serializer = PostSerializer(posts,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors,status=400)


@csrf_exempt
def post_by_id(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=404)

@csrf_exempt
def post_like(request,pk):
    try:
        post = Post.objects.get(pk=pk)
        post.likes += 1
        post.save()
        return HttpResponse(status=200)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

@csrf_exempt
def post_dislike(request,pk):
    try:
        post = Post.objects.get(pk=pk)
        post.likes -= 1
        post.save()
        return HttpResponse(status=200)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

@csrf_exempt
def post_insert_n_random_posts(request,n):
    if (request.method == 'GET'):
        for i in range(0,n):
            currPost = {'title': 'title number- ' +str(i), 'body': 'body number- ' + str(i), 'likes': i}
            serializer = PostSerializer(data=currPost)

            if serializer.is_valid():
                serializer.save()
            else:
                return JsonResponse(serializer.errors, status=400)

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)



