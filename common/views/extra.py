from rest_framework import generics

from ..serializers.extra import FAQSerializer, MainSettingsSerializer
from ..models import FAQ, MainSettings


class FAQListAPIView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
    pagination_class = None


class MainSettingsAPIView(generics.RetrieveAPIView):
    serializer_class = MainSettingsSerializer

    def get_object(self):
        return MainSettings.objects.first()

