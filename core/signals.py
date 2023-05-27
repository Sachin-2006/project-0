from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Story
from django.utils import timezone

@receiver(post_save,sender=Story)
def deletion_time(sender,instance,created,**kwargs):
	if created:
		expiration_period = timezone.timedelta(seconds=15)
		instance.delete_time = instance.created_at + expiration_period
		instance.save()

