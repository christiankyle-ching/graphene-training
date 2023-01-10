from django.urls import path
from books import views

urlpatterns = [
    path('', views.author_list),
    path('<int:pk>', views.author_detail),
]
