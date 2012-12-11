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
    url(r'^collection/', "website.views.secciones"),
    url(r'^campaign/', "website.views.campania"),
    url(r'^background/', "website.views.fondos"),
)
