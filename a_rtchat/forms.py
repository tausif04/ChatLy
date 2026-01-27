from django.forms import ModelForm
from a_rtchat.models import  GroupMessage
from django import forms

class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Type your message here...',
                'class': 'input input-bordered w-full max-w-xs',
                'maxlength': '300',
                'autofocus': True,
            }),
        } 