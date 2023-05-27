from celery import shared_task
from django.utils import timezone
from core.models import Story

@shared_task
def delete_expire_models():
	expired_models = Story.objects.filter(deletion_time__lt=timezone.now())
	expired_models.delete()