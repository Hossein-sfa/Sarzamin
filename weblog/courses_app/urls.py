from django.urls import path
from .views import *


urlpatterns = [
    path('list/', courses_list),
    path('<int:id>/', course_details),
    path('add/', add_course),
]
