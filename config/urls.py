from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.base.urls")),
    path("", include("apps.institute.urls")),
    path("", include("apps.sponsor.urls")),
    path("", include("apps.sponsor_summa.urls")),
    path("", include("apps.student.urls")),
    path("auth/", include("apps.accounts.urls")),

    re_path(r"media/(.*)", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"static/(.*)", serve, {"document_root": settings.STATIC_ROOT}),
]
