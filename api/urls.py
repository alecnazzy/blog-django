from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('topic-list/', views.topicList, name='topic-list'),
    path('topic-detail/<str:topic_id>/', views.topicDetail, name='topic-detail'),
    path('topic-create/', views.topicCreate, name='topic-create'),
    path('topic-update/<str:topic_id>/', views.topicUpdate, name='topic-update'),
    path('topic-delete/<str:topic_id>/', views.topicDelete, name='topic-delete'),
]