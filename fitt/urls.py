from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    path('',views.principal, name='index' ),
    path('accounts/registro/', RegistroView.as_view(), name="registro"),
]