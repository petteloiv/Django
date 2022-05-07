from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.moviedetail, name='moviedetail'),
    path('recommended/', views.recommended, name='recommended'),
]
