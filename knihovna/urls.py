"""knihovna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import django
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import knihovna_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('knihovna_app/', include('knihovna_app.urls')),
    path('', RedirectView.as_view(url='knihovna_app/')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'knihovna_app.views.error_404'
handler500 = 'knihovna_app.views.error_500'
handler403 = 'knihovna_app.views.error_403'
handler400 = 'knihovna_app.views.error_400'

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
    urlpatterns += [re_path(r'^500/$', knihovna_app.views.error_500)]
    urlpatterns += [re_path(r'^400/$', knihovna_app.views.error_400)]
    urlpatterns += [re_path(r'^404/$', knihovna_app.views.error_404)]
    urlpatterns += [re_path(r'^403/$', knihovna_app.views.error_403)]



admin.site.site_header = "ODK Administrace"
admin.site.site_title = "Online Databáze Knih"
admin.site.index_title = "Vítejte v administrační části ODK"
