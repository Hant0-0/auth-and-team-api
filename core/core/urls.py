from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from api_service.views import PeoplesAPI, PeopleAPI, TeamsAPI, TeamAPI


urlpatterns = [
    path('admin/', admin.site.urls),

    # API для людей
    path('api/peoples/', PeoplesAPI.as_view(), name='peoples-list'),
    path('api/peoples/<int:user_id>/', PeopleAPI.as_view(), name='people-list'),

    # API для команд
    path('api/teams/', TeamsAPI.as_view(), name='teams-list'),
    path('api/teams/<int:team_id>/', TeamAPI.as_view(), name='team-list'),


    # Google і Facebook автентифікацію
    path('', TemplateView.as_view(template_name='index.html')),
    path('accounts/', include('allauth.urls')),
    path('/', include("api_service.urls")),
]

