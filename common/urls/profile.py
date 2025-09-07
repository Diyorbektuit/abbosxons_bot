from django.urls import path

from common.views import profile as views


urlpatterns = [
    path('me/', views.UserProfileView.as_view()),
    path('transaction-history/', views.TransactionHistoryView.as_view()),
    path('payment-check/', views.PaymentCheckCreateView.as_view()),
]