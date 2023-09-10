from django.db.models.signals import post_save, post_delete
# from django.conf import settings
# from django.core.cache.utils import make_template_fragment_key
# from django.core.cache import caches, cache
from django.core.cache import cache
from blocks.models import BlockPrice, BlockSVG, BlockText
from bridges.models import Bridge
from contacts.models import Contacts
from images.models import Image
from index.models import Index
from porch.models import Porch, PorchTypicalProject
from railings.models import Railing
from staircases.models import Staircase, StaircaseTypicalProject
from terraces.models import Terrace, TerraceTypicalProject
from videos.models import Video


def receiver_multiple(signal, senders, **kwargs):
    """
    Based on django.dispatch.dispatcher.receiver

    Allows multiple senders so we can avoid using a stack of
    regular receiver decorators with one sender each.
    """

    def decorator(receiver_func):
        for sender in senders:
            if isinstance(signal, (list, tuple)):
                for s in signal:
                    s.connect(receiver_func, sender=sender, **kwargs)
            else:
                signal.connect(receiver_func, sender=sender, **kwargs)

        return receiver_func

    return decorator


senders = [
    BlockText, BlockPrice, BlockSVG, Contacts, Image, Video, Railing, Index,
    Staircase, Terrace, Porch, Bridge, TerraceTypicalProject, PorchTypicalProject,
    StaircaseTypicalProject,]
@receiver_multiple([post_save, post_delete], senders)
def cache_invalidate(instance, **kwargs):
    if kwargs.get('raw'):  # add for test, pass fixtures
        return

    cache.clear()

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


# @receiver(post_save, sender=Porch)
# def cache_invalidate(instance, **kwargs):
#     if kwargs.get('raw'):  # add for test, pass fixtures
#         return

#     # cache.delete('images')
#     # cache.delete_many(keys=cache.keys('images*'))
#     cache.clear()
