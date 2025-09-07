from rest_framework import generics

from core.permission import IsRegisteredPermission
from ..models import PaymentCheck
from ..serializers.profile import UserProfileSerializer, TransactionHistorySerializer, PaymentCheckCreateSerializer


class UserProfileView(generics.RetrieveAPIView):
    permission_classes = (IsRegisteredPermission, )
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.telegram_user


class TransactionHistoryView(generics.ListAPIView):
    permission_classes = (IsRegisteredPermission, )
    serializer_class = TransactionHistorySerializer

    def get_queryset(self):
        return self.request.telegram_user.transaction_history.all()


class PaymentCheckCreateView(generics.CreateAPIView):
    permission_classes = (IsRegisteredPermission, )
    serializer_class = PaymentCheckCreateSerializer
    queryset = PaymentCheck.objects.all()


