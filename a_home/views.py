from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from a_rtchat.models import ChatGroup
from a_rtchat.forms import ChatMessageCreateForm


def home_view(request):
    return render(request,'home.html')


# Create your views here.
def chat_view(request):
    chat_groups = ChatGroup.objects.all()
    form = ChatMessageCreateForm()
    context = {
        'chat_groups': chat_groups,
        'form': form,
    }
    return render(request, 'chat.html', context)
