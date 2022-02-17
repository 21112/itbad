from django.urls import path
from . import views

urlpatterns = [
    path('', views.usability_home, name='usabiliti-home'),
    path('what-is-usability', views.description_usability, name='description-usability')
    
]
