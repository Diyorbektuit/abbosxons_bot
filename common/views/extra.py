from rest_framework import generics

from ..serializers.extra import FAQSerializer
from ..models import FAQ


class FAQListAPIView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
    pagination_class = None

