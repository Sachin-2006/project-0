from django.core.managment.base import BaseCommand
from django.utils import timezone
from core.models import Story

class Command(BaseCommand):
    help = "Deletes"
    def handle(self,*args,**options):
	expired_models = Story.objects.filter(deletion_time__lt=timezone.now())
	expired_models.delete()
	self.stdout.write(self.style.SUCCESS('Expired models delted'))
