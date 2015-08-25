from django.conf.urls import patterns, include, url

from django.contrib import admin

from blogapp.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
    url(r'^article/(\d+)/',article_detail),
    url(r'^create_article/$',create_article),
    url(r'^submit_article/$',submit_article),
    url(r'^archives/(\d+)/',archives),
    url(r'^category/([A-Za-z]+)/',category),
    url(r'^login/$',login),
    url(r'^login_auth/$',login_auth),
)
