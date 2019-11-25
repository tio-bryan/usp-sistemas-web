from django.contrib import admin
from django.urls import path, include
from drive import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('drive/', views.index),
]