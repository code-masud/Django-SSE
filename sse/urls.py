from django.urls import path
from .views import index
app_name = 'sse'

urlpatterns = [
    path('sse', index, name="index")
]
