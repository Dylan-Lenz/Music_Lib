from django.urls import path
from songs import views

urlpatterns = [
    path('', views.get_all_songs),
    path('<str:pk>/', views.songs_by_id),
]