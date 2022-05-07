from django.urls import path
from . import views

app_name = 'commuinty'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.reviews, name='reviews'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/comments/create/', views.createcomment, name='createcomment'),
    path('<int:review_pk>/like/',views.like, name='like'),
]
