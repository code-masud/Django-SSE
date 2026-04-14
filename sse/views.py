from django.shortcuts import render
from django.http import JsonResponse
import asyncio
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User


async def async_home(request):
    # await asyncio.sleep(2)
    # user = await sync_to_async(User.objects.get)(id=1)
    # user = await get_user(1)
    user = await sync_to_async(get_user)(1)
    return JsonResponse({"user": user.username})


# @sync_to_async
# def get_user(id):
#     return User.objects.get(pk=id)

def get_user(id):
    return User.objects.get(pk=id)
