from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.getData),
    path('',views.getValues),
    path('add/',views.addValues),
]