from django.http import JsonResponse
from common.models import TelegramUser


class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get("X-API-KEY")

        if api_key:
            try:
                request.telegram_user = TelegramUser.objects.get(x_api_key=api_key)
            except TelegramUser.DoesNotExist:
                return JsonResponse({"error": "Invalid API Key"}, status=403)
        else:
            request.telegram_user = None

        return self.get_response(request)
