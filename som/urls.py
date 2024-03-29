from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.shortcuts import render
from index.views import index
from index.sitemap import IndexSitemap
from bridges.sitemap import BridgeSitemap
from bridges.views import bridges
from contacts.sitemap import ContactsSitemap
from contacts.views import contacts
from porch.sitemap import PorchSitemap
from railings.sitemap import RailingSitemap
from staircases.sitemap import StaircaseSitemap
from terraces.sitemap import TerraceSitemap
from terraces.views import terraces

sitemaps = {
    'index': IndexSitemap,
    'staircase': StaircaseSitemap,
    'railing': RailingSitemap,
    # 'steps': StepsSitemap,
    'terrace': TerraceSitemap,
    'porch': PorchSitemap,
    'bridge': BridgeSitemap,
    'contacts': ContactsSitemap,
}


urlpatterns = [
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='/admin/login'), name='logout'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('decorative-bridge/', bridges, name='decorative-bridge'),
    path('terrace/', terraces, name='terrace'),
    path('callback/', include(('callback.urls', 'callback'), namespace='callback')),
    path('staircases/', include(('staircases.urls', 'staircases'), namespace='staircases')),
    path('railings/', include(('railings.urls', 'railings'), namespace='railings')),
    path('porch/', include(('porch.urls', 'porch'), namespace='porch')),
    # path('steps/', include(('steps.urls', 'steps'), namespace='steps')),
    path('privacy-policy/', TemplateView.as_view(
        template_name="privacy-policy/index.html"), name="privacy-policy"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]

admin.site.site_header = admin.site.site_title = 'ПМ «Студия Металла»'

def handler400(request, exception, template_name='errors/400.html'):
    response = render(request, template_name)
    response.status_code = 400
    return response


def handler403(request, exception, template_name='errors/403.html'):
    response = render(request, template_name)
    response.status_code = 403
    return response


def handler404(request, exception, template_name='errors/404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response

# def handler404(request, exception):
#     return render(request, 'errors/404.html', status=404)


def handler500(request, template_name='errors/500.html'):
    response = render(request, template_name)
    response.status_code = 500
    return response


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    urlpatterns += [
        path('400/', TemplateView.as_view(template_name="errors/400.html")),
        path('403/', TemplateView.as_view(template_name="errors/403.html")),
        path('404/', TemplateView.as_view(template_name="errors/404.html")),
        path('500/', TemplateView.as_view(template_name="errors/500.html")),
    ]

    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(r'/favicon.ico', document_root='static/favicon.ico')
    # urlpatterns += static(r'/site.webmanifest', document_root='static/site.webmanifest')
