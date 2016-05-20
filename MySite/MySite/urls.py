"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article_content/(\d+)/?$', 'my_blog.views.show_article_content', name='article_content'),
    url(r'^create_article/?$', "my_blog.views.create_article", name="create_article"),
    url(r'^$', 'my_blog.views.article', name='article'),
    url(r'^blog/?$', 'my_blog.views.article', name='article'),
    url(r'^login/$', 'my_blog.views.login',name='login'),
    url(r'^logout/$', 'my_blog.views.logout',name='logout'),
    url(r'^show_tag/(\d+)$', 'my_blog.views.show_tag',name='show_tag'),
    url(r'^show_genre/(\d+)$', 'my_blog.views.show_genre',name='show_genre'),
]
