from django.utils import timezone

from rest_framework import serializers

from ..models import TelegramUser, TransactionHistory, TelegramUserSubscribed


class UserProfileSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()
    rest_of_days = serializers.SerializerMethodField()

    class Meta:
        model = TelegramUser
        fields = (
            'is_subscribed',
            'rest_of_days'
        )
        read_only_fields = fields

    @staticmethod
    def get_is_subscribed(obj):
        if not hasattr(obj, 'subscribed'):
            return False
        return obj.subscribed.expired_at > timezone.now()

    @staticmethod
    def get_rest_of_days(obj):
        if not hasattr(obj, 'subscribed'):
            return 0
        if obj.subscribed.expired_at < timezone.now():
            return 0
        return (obj.subscribed.expired_at - timezone.now()).days


class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = (
            'amount',
            'created_at'
        )
        read_only_fields = fields


