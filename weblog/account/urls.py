from django.urls import path
from .views import *


urlpatterns = [
    path('', users),
    path('<username>/', profile),
]
