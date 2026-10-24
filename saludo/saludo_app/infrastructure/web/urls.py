from django.urls import path
from saludo_app.infrastructure.web.views import saludar_view

urlpatterns = [
    path('saludar/', saludar_view),
]