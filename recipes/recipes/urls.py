from django.urls import path
from calculator.views import recipe_view

urlpatterns = [
    path('<recipe_name>/', recipe_view)
]
