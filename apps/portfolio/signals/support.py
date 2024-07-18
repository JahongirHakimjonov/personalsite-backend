from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.portfolio.models import Support


@receiver(pre_save, sender=Support)
def send_email_on_answer(sender, instance, **kwargs):
    if instance.answer and not instance.is_read:
        send_mail(
            subject="Murojaat uchun rahmat !!!",
            message=instance.answer,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
        )
        print(f"Email sent to {instance.email}")
        instance.is_read = True
        instance.save()
