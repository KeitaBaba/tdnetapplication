from django.urls import path
from . import views

app_name = 'tdnet'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('tdnet/index', views.index, name='index'),
    path('tdnet/new', views.new, name='new'),
    path('tdnet/error', views.customer_models, name='error'),
    path('tdnet/create', views.customer_models, name='create'),
]