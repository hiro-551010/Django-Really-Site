"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# --- sitemap ---
from django.contrib.sitemaps.views import sitemap
from config.sitemaps import StaticViewSitemap, BlogSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}
# --- sitemap ---

# viewsがdefなら関数名
# classならクラス名とas_view()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),

    path('', include('mysite.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    name="django.contrib.sitemaps.views.sitemap")
]

"""

urlごとにキャッシュできる
from django.views.decorators.cache import cache_page

ex)    
path('admin/', cache_page(30)(admin.site.urls)),

"""