from . import stat
from . import gene
from . import variant
from .util import web

# Create your views here.


def home(request):
    data = {}
    return web.render(request, 'index.html', data)


def gene_list(request):
    data = {}
    return web.render(request, 'gene_list.html', data)


def gene_view(request):
    data = {}
    return web.render(request, 'gene_view.html', data)


def variant_list(request):
    data = {}
    return web.render(request, 'variant_list.html', data)


def variant_view(request):
    data = {}
    return web.render(request, 'variant_view.html', data)


def stat_view(request):
    data = {}
    return web.render(request, 'stat_list.html', data)
