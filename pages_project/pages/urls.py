from django.urls import path 
from .views import homepage,aboutpage

urlpatterns =[
    path('', homepage.as_view(), name = 'home'),
    path('about/', aboutpage.as_view(), name = 'about'),
]