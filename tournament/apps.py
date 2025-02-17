from django.apps import AppConfig

class TournamentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tournament'

    def ready(self):
        import tournament.signals  # This ensures signals are connected when Django starts