from django.urls import path
from .views import async_home
app_name = 'sse'

urlpatterns = [
    path('sse', async_home, name="index")
]
