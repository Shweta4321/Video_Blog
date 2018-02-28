from django.conf.urls import url
from . import views


app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),


    #/music/<album_id>
    url(r'^(?P<pk>[0-9]+)/$',views.DetailsView.as_view(), name='details'),

    #/music/album/add
    url(r'album/add/$',views.AddAlbum.as_view(), name='Add_Album'),

    #/music/<album_id>/2
    url(r'album/(?P<pk>[0-9]+)/$',views.UpdateAlbum.as_view(), name='album-update'),

    url(r'album/(?P<pk>[0-9]+)/delete/$',views.DeleteAlbum.as_view(), name='delete_album'),

    #url(r'album/add/fav$',views.DetailsView.as_view(), name='favorite_album'),






]