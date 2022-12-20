from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    try:
        print("MODEL")
        print(instance)
        if created:
            Token.objects.create(user=instance)
    except Exception as e:
        raise e
    