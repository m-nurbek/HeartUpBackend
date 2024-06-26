from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include('authentication.urls')),
    path('users/', include('core_app.urls')),
    path('api/ml/', include('machine_learning_app.urls')),
    path('api/appointment/', include('appointment.urls')),
    path('api/notification/', include('notification.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
