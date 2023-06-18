from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.conf import settings
# from django.core.cache.utils import make_template_fragment_key
# from django.core.cache import caches, cache
from django.core.cache import cache
from django.db.models.signals import post_save
from blocks.models import BlockPrice, BlockSVG, BlockText
from bridges.models import Bridge
from contacts.models import Contacts
from images.models import Image
from index.models import Index
from porch.models import Porch
from railings.models import Railing
from staircases.models import Staircase
from terraces.models import Terrace
from videos.models import Video


@receiver(post_save, sender=BlockText)
@receiver(post_save, sender=BlockPrice)
@receiver(post_save, sender=BlockSVG)
@receiver(post_save, sender=Contacts)
@receiver(post_save, sender=Image)
@receiver(post_save, sender=Video)
@receiver(post_save, sender=Railing)
@receiver(post_save, sender=Index)
@receiver(post_save, sender=Staircase)
@receiver(post_save, sender=Terrace)
@receiver(post_save, sender=Porch)
@receiver(post_save, sender=Bridge)
def cache_invalidate(instance, **kwargs):
    if kwargs.get('raw'):  # add for test, pass fixtures
        return

    # fragment_names = [
    #     'gridview_object',
    #     'listview_object',
    #     'description_table',
    #     'detail_image',
    #     'detail_head',
    # ]

    # for value in fragment_names:
    #     for language_code, lang in settings.LANGUAGES:
    #         key = make_template_fragment_key(
    #             '{0}_{1}'.format(instance._meta.model_name, value), [
    #                 instance.id, language_code]
    #         )
    #         caches[instance._meta.model_name].delete(key)

    # print(instance._meta.app_label)
    # key = make_template_fragment_key('images', [instance._meta.app_label, instance.id])
    # caches['images'].delete(key)
    # caches['images'].remove()
    cache.clear()

# @receiver(post_save, sender=Porch)
# def cache_invalidate(instance, **kwargs):
#     if kwargs.get('raw'):  # add for test, pass fixtures
#         return

#     # cache.delete('images')
#     # cache.delete_many(keys=cache.keys('images*'))
#     cache.clear()
