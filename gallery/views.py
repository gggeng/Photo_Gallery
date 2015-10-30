from django.shortcuts import render, render_to_response
from models import Item, Photo
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    def get_queryset(self):
        return Item.objects.all()[:3]


class ListView(generic.ListView):
    model = Item
    template_name = 'items_list.html'


class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'items_detail.html'


class PhotoDetailView(generic.DetailView):
    model = Photo
    template_name = 'photos_detail.html'