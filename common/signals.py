from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.cache.utils import make_template_fragment_key
from django.core.cache import caches, cache
from django.db.models.signals import post_save
from bridges.models import Bridge
from index.models import IndexPage
from porch.models import Porch
from staircases.models import Staircase
from steps.models import Steps


@receiver(post_save, sender=IndexPage)
@receiver(post_save, sender=Staircase)
@receiver(post_save, sender=Steps)
@receiver(post_save, sender=Porch)
@receiver(post_save, sender=Bridge)
def cache_invalidate(instance, **kwargs):
    """ Rule of naming cache template fragment: time, model_name + fragment name, object_id, language_code """
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

    print(instance._meta.app_label)
    key = make_template_fragment_key('images', [instance._meta.app_label, instance.id])
    caches['images'].delete(key)
    # caches['images'].remove()


# @receiver(post_save, sender=Porch)
# def cache_invalidate(instance, **kwargs):
#     if kwargs.get('raw'):  # add for test, pass fixtures
#         return

#     # cache.delete('images')
#     # cache.delete_many(keys=cache.keys('images*'))
#     cache.clear()
