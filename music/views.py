from django.views import generic
from .models import Album,Song
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = 'all_album'

    def get_queryset(self):
        return  Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album
    template_name = "music/details.html"

class AddAlbum(CreateView):
    model = Album
    fields = ['Artist','album_title','Genere','album_logo']

class UpdateAlbum(UpdateView):
    model = Album
    fields = ['Artist', 'album_title', 'Genere', 'album_logo']

class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

