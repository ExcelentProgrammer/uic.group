from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(

    openapi.Info(
        title="Azamov Samandar",
        default_version='v1',
        description="Django api",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="azamov.samandar.programmer@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("", include("apps.base.urls")),
    path("", include("apps.institute.urls")),
    path("", include("apps.sponsor.urls")),
    path("", include("apps.sponsor_summa.urls")),
    path("", include("apps.student.urls")),
    path("auth/", include("apps.accounts.urls")),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    re_path(r"media/(.*)", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"static/(.*)", serve, {"document_root": settings.STATIC_ROOT}),
]
