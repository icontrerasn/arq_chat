from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Message
from .forms import ChatForm
from ipware import get_client_ip
import datetime

@csrf_exempt
def index(request):
    messages = Message.objects.order_by('-pub_date')[:6]
    form = ChatForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            text = form.cleaned_data['message']
            new_message = Message(text = text, pub_date = datetime.datetime.now(), ip = get_client_ip(request)[0])
            new_message.save()
    return render(request, 'chat.html', {'form': form, 'messages': messages})
