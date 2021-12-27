
from django.urls import path
from . import views
urlpatterns = [
    path('', views.bi_process,name="bi"),
    path('map/', views.map_process,name="map")
]
