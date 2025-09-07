from rest_framework import serializers

from ..models import FAQ, MainSettings


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = (
            'question',
            'answer'
        )
        read_only_fields = fields


class MainSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSettings
        fields = '__all__'
