from django.urls import path
from songs import views

urlpatterns = [
    path('', views.songs_by_obj),
    path('<int:pk>/', views.songs_by_id),
]