from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name='public-chat')
    chat_messages = chat_group.chat_message.all()[:30]
    form = ChatMessageCreateForm()

    if request.htmx:
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.author = request.user
            new_message.group = chat_group
            new_message.save()
            context = {'chat_message': new_message,
                       'user' : request.user
                       }
            return render(request, 'a_rtchat/partials/chat_message_p.html', context) # Redirect to avoid resubmission
    return render(request, 'a_rtchat/chat.html', { 'chat_messages': chat_messages, 'form': form })