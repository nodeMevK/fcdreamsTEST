from django.contrib import admin
from .models import Tournament, Team, Match, Result

admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(Result)