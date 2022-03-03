from django import path
from . import views

urlpatterns = [
    path('lotto/', views.lotto),
]
