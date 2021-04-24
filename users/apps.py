#
# Configure the Users app
#

from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'
    
    # Import the signals for the Users app
    def ready(self):
        import users.signals
