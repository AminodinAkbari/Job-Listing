from django.db.models.signals import pre_save , pre_delete
from django.dispatch import receiver
from Blog.models import MainBlogModule
import os

@receiver(pre_save, sender=MainBlogModule)
def delete_old_file(sender, instance, **kwargs):
    print('signal')
    # detect user creation or updated
    # When a User Create , Have'nt pk.  
    if instance._state.adding and not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).banner
    except sender.DoesNotExist:
        return False

    # comparing the new file with the old one
    file = instance.banner
    if not old_file == file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

@receiver(pre_delete , sender = MainBlogModule)
def delete_banner_when_deleted(sender , instance , **kwargs):
    # When A Query Deleted , The Banner In Banners Folder Delted
    try:
        file = sender.objects.get(pk = instance.id).banner
    except:
        file = None
        return False
    if file is not None:
        if os.path.isfile(file.path):
            os.remove(file.path)
