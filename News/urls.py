from django.urls import path
from .views import index, new, by_rubric

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index),
    path('new', new, name='NewsIndex'),
]