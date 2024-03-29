from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cadastro/', include('cadastro.urls')),
    path('contas/', include('contas.urls')),
    path('calendario/', include('calendario.urls')),
    path('uniforme/', include('uniforme.urls')),
    path('space/', include('space.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
