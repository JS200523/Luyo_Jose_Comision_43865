from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/')
    description = models.TextField()
    website = models.URLField()


class Message(models.Model):
    recipient = models.ForeignKey(User, related_name='received_messages_account', related_query_name='received_message_account', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages_account', related_query_name='sent_message_account', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    