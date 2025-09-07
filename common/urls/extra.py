from django.urls import path

from ..views import extra as views


urlpatterns = [
    path('faq/', views.FAQListAPIView.as_view()),
    path('main-settings/', views.MainSettingsAPIView.as_view())
]