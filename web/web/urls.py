"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from web.admin_site import admin_site
from web.feeds import webFeed
from web.sitemap import CategorySiteMap, ArticleSiteMap, TagSiteMap, UserSiteMap, StaticViewSitemap

sitemaps = {

    'blog': ArticleSiteMap,
    'Category': CategorySiteMap,
    'Tag': TagSiteMap,
    'User': UserSiteMap,
    'static': StaticViewSitemap
}

handler404 = 'blog.views.page_not_found_view'
handler500 = 'blog.views.server_error_view'
handle403 = 'blog.views.permission_denied_view'
urlpatterns = [
                  path(r'demo/', include('demoapp.urls')),
                  url(r'^admin/', admin_site.urls),
                  url(r'', include('blog.urls', namespace='blog')),
                  url(r'mdeditor/', include('mdeditor.urls')),
                  url(r'', include('comments.urls', namespace='comment')),
                  url(r'', include('accounts.urls', namespace='account')),
                  url(r'', include('oauth.urls', namespace='oauth')),
                  url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                      name='django.contrib.sitemaps.views.sitemap'),
                  url(r'^feed/$', webFeed()),
                  url(r'^rss/$', webFeed()),
                  url(r'^search', include('haystack.urls'), name='search'),
                  url(r'', include('servermanager.urls', namespace='servermanager')),
                  url(r'', include('owntracks.urls', namespace='owntracks'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
