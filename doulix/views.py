from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import random
import time


# Create your views here.
def index(request):
    return render(request, 'doulix/index.html')


def webservice(request):
    layer = get_channel_layer()
    i = 0
    while(i < 100):
        async_to_sync(layer.group_send)("doulix", {
            'type': 'chat_message',
            'message': random.randint(1, 9999)
        })
        time.sleep(random.randint(1, 99))
        i += 1
    return HttpResponse('done')
