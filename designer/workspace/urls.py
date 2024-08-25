from django.urls import path
from .views import canvas_editor_view

urlpatterns = [
    path('', canvas_editor_view, name='canvas_editor'),
]
