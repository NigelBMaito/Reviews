from django.urls import path
from . import views

app_name = 'deals'
urlpatterns = [
    path('packages/', views.deals_view, name= 'packages')
]
