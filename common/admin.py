from django.contrib import admin
from .models import TelegramUser, TelegramUserSubscribed, TransactionHistory


# Register your models here.
@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ("telegram_user_id", "created_at", "updated_at")
    search_fields = ("telegram_user_id",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(TelegramUserSubscribed)
class TelegramUserSubscribedAdmin(admin.ModelAdmin):
    list_display = ("telegram_user", "expired_at", "created_at", "updated_at")
    search_fields = ("telegram_user__telegram_user_id",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(TransactionHistory)
class TransactionHistoryAdmin(admin.ModelAdmin):
    list_display = ("telegram_user", "amount", "created_at", "updated_at")
    search_fields = ("telegram_user__telegram_user_id",)
    readonly_fields = ("created_at", "updated_at")
