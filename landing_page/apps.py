from django.apps import AppConfig


class home_pageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landing_page'

class MenuesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menues'

class LocationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'location'      

