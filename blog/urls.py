from django.conf.urls import patterns, include, url
from django.conf import settings
from blog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lynn_isaac.views.home', name='home'),
    # url(r'^lynn_isaac/', include('lynn_isaac.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name='index'),
    #url(r'^stories/(?P<post_title_url>\w+)/$', views.story, name='story'),
    url(r'^stories/(\d)/$', views.story, name='story'),
    url(r'^stories/$', views.stories, name='stories'),

)
