from django.urls import path

from api_service import views

urlpatterns = [
    path("", views.home, name='home'),
    path("logout/", views.logout_view, name='logout_view'),

]