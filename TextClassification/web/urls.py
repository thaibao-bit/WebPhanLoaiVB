from os import name
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name= "home"),
    path('textclf/', text_classification, name="textclf"),
    path('linkclf/', link_classification, name= "linkclf"),
    path('label/<str:label>/', get_by_label, name= "label" ),
    path('about/', about, name="about")
]