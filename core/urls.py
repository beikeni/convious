
from django.urls import path, include
from . import views
from .router import router

app_name = 'core'
urlpatterns = [
    path('vote/', views.VoteAPIView.as_view(), name="vote"),
    path('result/', views.ResultAPIView.as_view(), name="result"),
    path('', include(router.urls))
]