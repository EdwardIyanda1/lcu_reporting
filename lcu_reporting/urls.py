from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def healthz(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
     path("healthz", healthz),
    path('admin/', admin.site.urls),
    path('', include('reports.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
