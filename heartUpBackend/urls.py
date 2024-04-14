from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('core-app/', include('core_app.urls')),
    path('api/data/', include('medical_data.urls')),
    path('api/ml/', include('machine_learning_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
