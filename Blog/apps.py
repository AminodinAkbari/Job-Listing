from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blog'

class DeleteOldImage(AppConfig):
    name = 'Blog'
    def ready(self):
        from Blog.signals import delete_old_file , delete_banner_when_deleted
