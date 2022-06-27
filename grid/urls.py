from django.urls import path
from .views import index, get_employer, get_visit_day, add_visit

urlpatterns = [
    path('', index, name='index'),
    path('employer/<str:slug>', get_employer, name='employer'),
    path('list-visit/', get_visit_day, name='get_visit_day'),
    path('add-visit/', add_visit, name='add_visit')
]


