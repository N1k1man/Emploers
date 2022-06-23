from django.urls import path
from .views import index, get_employer

urlpatterns = [
    path('', index, name='index'),
    path('employer/<str:slug>', get_employer, name='employer')
]

