from django.shortcuts import render
from django.http import HttpResponse
import asyncio


async def index(request):
    await asyncio.sleep(1)
    return HttpResponse('Hello World!')
