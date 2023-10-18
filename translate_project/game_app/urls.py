from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.game_index, name="game_index"),
    # path('drag_drop/<int:pk>/', views.drag_drop, name="drag_drop"), # pk : 언어코드
    path('drag_drop/<int:lang>/<int:stage>/', views.drag_drop, name="drag_drop"), # pk : 언어코드
]
