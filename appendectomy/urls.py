from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^', include('提議連署.網址')),

#     url(r'^admin/', include(admin.site.urls)),
)
