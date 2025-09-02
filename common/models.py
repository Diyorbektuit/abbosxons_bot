import uuid

from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TelegramUser(BaseModel):
    telegram_user_id = models.BigIntegerField(unique=True)
    x_api_key = models.CharField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"TelegramUser: {self.telegram_user_id}"

    def save(self, *args, **kwargs):
        if not self.x_api_key:
            self.x_api_key = uuid.uuid4()
        super().save(*args, **kwargs)


class TelegramUserSubscribed(BaseModel):
    telegram_user = models.OneToOneField(TelegramUser, on_delete=models.CASCADE, related_name="subscribed")
    expired_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"TelegramUserSubscribed: {self.telegram_user}"


class TransactionHistory(BaseModel):
    telegram_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name="transaction_history")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"TransactionHistory: {self.telegram_user}"


class FAQ(BaseModel):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"FAQ: {self.question}"





