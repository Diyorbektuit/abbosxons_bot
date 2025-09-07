from django.utils import timezone
from datetime import timedelta

from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import TelegramUser, TelegramUserSubscribed, TransactionHistory, FAQ, PaymentCheck, MainSettings
from .utils import create_invite_link, send_telegram_bot_message


admin.site.unregister(User)
admin.site.unregister(Group)


# Register your models here.
@admin.register(MainSettings)
class MainSettingsAdmin(admin.ModelAdmin):
    list_display = ("main_subscription_price", )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ("telegram_user_id", "created_at", "updated_at")
    search_fields = ("telegram_user_id",)
    readonly_fields = ("created_at", "updated_at")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(TelegramUserSubscribed)
class TelegramUserSubscribedAdmin(admin.ModelAdmin):
    list_display = ("telegram_user", "expired_at", "created_at", "updated_at")
    search_fields = ("telegram_user__telegram_user_id",)
    readonly_fields = ("created_at", "updated_at", "telegram_user")

    def has_add_permission(self, request):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

@admin.register(TransactionHistory)
class TransactionHistoryAdmin(admin.ModelAdmin):
    list_display = ("telegram_user", "amount", "created_at", "updated_at")
    search_fields = ("telegram_user__telegram_user_id",)
    readonly_fields = ("created_at", "updated_at")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at", "updated_at")
    search_fields = ("question",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(PaymentCheck)
class PaymentCheckAdmin(admin.ModelAdmin):
    list_display = ("telegram_user", "payment_check", "status", "created_at")
    list_filter = ("status", "telegram_user")
    readonly_fields = ("created_at", "updated_at", "payment_check", "telegram_user")

    def has_add_permission(self, request):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def save_model(self, request, obj, form, change):
        old_status = None
        if obj.pk:
            old_status = PaymentCheck.objects.filter(pk=obj.pk).values_list("status", flat=True).first()

        super().save_model(request, obj, form, change)

        if old_status != "accepted" and obj.status == "accepted":
            main_subscription_price = MainSettings.objects.first().main_subscription_price

            subscribed, created = TelegramUserSubscribed.objects.get_or_create(
                telegram_user=obj.telegram_user,
                defaults={"expired_at": timezone.now() + timedelta(days=30)},
            )
            if not created:
                if subscribed.expired_at < timezone.now():
                    subscribed.expired_at = timezone.now() + timedelta(days=30)
                else:
                    subscribed.expired_at += timedelta(days=30)
                subscribed.save()

            link = create_invite_link()
            send_telegram_bot_message(obj.telegram_user.telegram_user_id, link)

            TransactionHistory.objects.create(
                telegram_user=obj.telegram_user,
                amount=main_subscription_price,
            )

