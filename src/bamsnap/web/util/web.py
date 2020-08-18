from .. import conf
import random
import django.shortcuts


def render(request, template, data={}):
    ndata = {}
    ndata['TITLE'] = conf.TITLE
    ndata['randkey'] = random.randint(10**8, 10**9)
    ndata['errmsg'] = ""
    if "errmsg" in request.GET.keys():
        ndata['errmsg'] = request.GET['errmsg'].strip()

    ndata['sampleselect_cookie'] = request.COOKIES.get('sampleselect', {})

    for k1 in data.keys():
        ndata[k1] = data[k1]
    return django.shortcuts.render(request, template, ndata)
