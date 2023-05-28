"""som URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from bridges.sitemap import BridgeSitemap
from bridges.views import bridges
from contacts.sitemap import ContactsSitemap
from index.sitemap import IndexSitemap
from index.views import index
from contacts.views import contacts
from django.views.generic import TemplateView
from porch.sitemap import PorchSitemap
from django.shortcuts import render
from staircases.sitemap import StaircaseSitemap
from steps.sitemap import StepsSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'index': IndexSitemap,
    'staircase': StaircaseSitemap,
    'steps': StepsSitemap,
    'porch': PorchSitemap,
    'contacts': ContactsSitemap,
    'bridges': BridgeSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('crossing-bridge/', bridges, name='bridges'),
    path('callback/', include(('callback.urls', 'callback'), namespace='callback')),

    path('staircases/', include(('staircases.urls',
         'staircases'), namespace='staircases')),

    path('railing/', include(('railing.urls',
         'railing'), namespace='railing')),

    # path('<slug:slug>/', staircase, name='staircase'),
    # path('<slug>/', staircase, name='staircase'),

    # path('porch/', include(('porch.urls', 'porch'), namespace='porch')),
    # path('<slug>/', porch, name='porch'),

    path('porch/', include(('porch.urls',
         'porch'), namespace='porch')),

    # path('steps/', include(('steps.urls', 'steps'), namespace='steps')),
    # path('<slug>/', steps, name='steps'),

    path('steps/', include(('steps.urls',
         'steps'), namespace='steps')),

    path('privacy-policy/', TemplateView.as_view(
        template_name="privacy-policy/privacy-policy.html"), name="privacy-policy"),
        
    path('martor/', include('martor.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]


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