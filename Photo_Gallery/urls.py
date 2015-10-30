from django.conf.urls import patterns, include, url
from django.contrib import admin
from gallery import views
from Photo_Gallery import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Photo_Gallery.views.home', name='home'),
    # url(r'^Photo_Gallery/', include('Photo_Gallery.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/?P.*$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^items/$', views.ListView.as_view(), name='item_list'),
    url(r'^items/(?P<pk>\d+)/$', views.ItemDetailView.as_view(), name='item_detail'),
    url(r'^photos/(?P<pk>\d+)/$', views.PhotoDetailView.as_view(), name='photo_detail'),

)
