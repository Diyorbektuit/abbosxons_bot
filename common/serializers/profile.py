from django.utils import timezone

from rest_framework import serializers

from ..models import TelegramUser, TransactionHistory, PaymentCheck


class UserProfileSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()
    rest_of_days = serializers.SerializerMethodField()

    class Meta:
        model = TelegramUser
        fields = (
            'is_subscribed',
            'rest_of_days',
        )
        read_only_fields = fields

    @staticmethod
    def get_is_subscribed(obj):
        if not hasattr(obj, 'subscribed'):
            return "no_subscribed"
        elif obj.subscribed.expired_at < timezone.now():
            return "expired"
        else:
            return "subscribed"

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


class PaymentCheckCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCheck
        fields = (
            'payment_check',
        )

    def validate(self, attrs):
        telegram_user = self.context['request'].telegram_user
        if PaymentCheck.objects.filter(telegram_user=telegram_user, status=PaymentCheck.StatusChoice.pending).exists():
            raise serializers.ValidationError("Sizda hozirda tekshirilayotgan to'lov mavjud")
        return attrs

    def create(self, validated_data):
        telegram_user = self.context['request'].telegram_user
        payment_check = PaymentCheck.objects.create(
            telegram_user=telegram_user,
            payment_check=validated_data['payment_check'],
            status=PaymentCheck.StatusChoice.pending
        )
        return payment_check




