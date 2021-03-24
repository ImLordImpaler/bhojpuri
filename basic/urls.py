from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homepage , name='homepage'),
    path('videoDetail/<str:pk>/' , views.videoDetail , name='videoDetail')
]