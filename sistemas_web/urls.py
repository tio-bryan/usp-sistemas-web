from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from drive import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('drive/', TemplateView.as_view(template_name='drive.html'), name='home'),
    # path('drive/', views.index),
]