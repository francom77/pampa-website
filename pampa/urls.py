from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

	# Vista para el index
	url(r'^$', 'website.views.index'),

	# Vistas del admin
    url(r'^admin/', include(admin.site.urls)),

    # Vistas json
    url(r'^collection/(?P<id_seccion>\d+)$', 'website.views.productos'),
    url(r'^collectionMan/', "website.views.seccionesHombre"),
    url(r'^collectionWoman/', "website.views.seccionesMujer"),
    url(r'^campaign/', "website.views.campania"),
    url(r'^background/', "website.views.fondos"),
    url(r'^contacto/', "website.views.contacto"),
    url(r'^subscribe/', "website.views.suscriptor"),
)


# Configuraciones adicionales para servir archivos media,
# cuando trabajamos con el servidor de desarrollo
import settings
if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                serve,
                                {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)