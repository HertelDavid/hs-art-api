from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:page_number>', views.get_page, name='get_page')
]