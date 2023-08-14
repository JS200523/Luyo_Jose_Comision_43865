from django.db import models
from django.contrib.auth.models import User 

class Message(models.Model):
    recipient = models.ForeignKey(User, related_name='received_messages_message', related_query_name='received_message_message', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages_message', related_query_name='sent_message_message', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient}"

    class Meta:
        app_label = 'messages'