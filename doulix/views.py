from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync, sync_to_async
import random
import time
import asyncio


# Create your views here.
def index(request):
    return render(request, 'doulix/index.html')


async def main():
    layer = get_channel_layer()
    while True:
        await layer.group_send("doulix", {
            'type': 'chat_message',
            'message': random.randint(1, 9999)
        })
        await asyncio.sleep(random.randint(1, 99))
    return None


def webservice(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    return None
