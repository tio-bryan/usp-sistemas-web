from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from drive import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='drive.html'), name='home'),
    path('', views.index),
    path('delete/<int:id>', views.remove),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)