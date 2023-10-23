from django.contrib import admin

from api_service.models import Team, People


admin.site.register(Team)


class PeopleAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'team']
    list_filter = ['team']


admin.site.register(People, PeopleAdmin)
