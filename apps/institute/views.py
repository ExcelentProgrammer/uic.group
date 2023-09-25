from django.shortcuts import render
from rest_framework.generics import ListAPIView

from apps.institute.models import Institute
from apps.institute.serializers import InstituteSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class InstituteListApi(ListAPIView):
    """Institute List View"""

    model = Institute
    serializer_class = InstituteSerializer
    queryset = Institute.objects.order_by("id")
    filterset_fields = ["name"]

    @method_decorator(cache_page(60 * 1))
    def dispatch(self, request, *args, **kwargs):
        """Cache vaqtini kamaytirish uchun 1 daqiqa"""

        return super().dispatch(request, *args, **kwargs)
