
from django.contrib import admin
from django.urls import path
from apps import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dev/', views.dev),
    path('dev2/', views.dev2),
]
