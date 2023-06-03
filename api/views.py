from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required

from .serializers import TopicSerializer
from blog.models import Topic

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/topic-list/',
        'Detail View': '/topic-detail/<str:pk>/',
        'Create': '/topic-create/',
        'Update': '/topic-update/<str:pk>/',
        'Delete': '/topic-delete/<str:pk>/',
    }
    return Response(api_urls)

@login_required
@api_view(['GET'])
def topicList(request):
    topics = Topic.objects.all().order_by('-id')
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def topicDetail(request, topic_id):
    topics = Topic.objects.get(id=topic_id)
    serializer = TopicSerializer(topics, many=False)
    return Response(serializer.data)

@login_required
@api_view(['POST'])
def topicCreate(request):
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@login_required
@api_view(['POST'])
def topicUpdate(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    serializer = TopicSerializer(instance=topic, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@login_required
@api_view(['DELETE'])
def topicDelete(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    return Response('Item successfully deleted!')
