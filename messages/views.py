from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message


def message_view(request):
    messages = Message.objects.all()
    return render(request, 'messages/messages.html', {'messages': messages})

@login_required
def message_list(request):
    received_messages = request.user.received_messages.all()
    return render(request, 'messages/message_list.html', {'messages': received_messages})

@login_required
def create_message(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        body = request.POST['body']
        message = Message.objects.create(sender=request.user, recipient=recipient, subject=subject, body=body)
        return redirect('message_list')
    else:
        return render(request, 'messages/create_message.html')

@login_required
def view_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'messages/view_message.html', {'message': message})