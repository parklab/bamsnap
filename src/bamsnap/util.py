import os
import sys
import time
import bamsnap
import json
from PIL import ImageColor
if (sys.version_info > (3, 0)):
    from html.parser import HTMLParser
    from urllib.parse import urlparse
    import urllib.request
else:
    from HTMLParser import HTMLParser
    import urlparse

def init_dict(dict1, key1):
    try:
        dict1[key1]
    except KeyError:
        dict1[key1] = {}
    return dict1


def add_dict_value(dict1, key1, add_vale=1):
    try:
        dict1[key1] += add_vale
    except KeyError:
        dict1[key1] = add_vale
    return dict1

def get_scale(x1, x2, width):
    scale = 1.0 * width / abs(x2 - x1)
    return scale

def getrgb(hexcode, whitening=0):
    rgb = ImageColor.getrgb("#" + hexcode)
    if whitening > 0:
        rgb = (rgb[0] + whitening, rgb[1] + whitening, rgb[2] + whitening)
    return rgb


def convert_int_list(strlist):
    intlist = []
    for s1 in strlist:
        if s1 != '':
            try:
                intlist.append(int(s1))
            except ValueError:
                pass
    return intlist

def comma(value):
    return "{:,}".format(value)

def mkDir(dpath):
    if not os.path.isdir(dpath):
        os.mkdir(dpath)

def decodeb(bstr):
    if type(bstr)== type(b'a'):
        rst = bstr.decode('UTF-8')
    else:
        rst = bstr
    return rst

def check_dir(fname):
    if fname[0] != '/' and fname[0] != '.':
        fname = './' + fname
    arr = fname.split("/")
    fpath = arr[0]
    for d in arr[1:-1]:
        fpath += "/" + d
        if not is_exist(fpath):
            mkDir(fpath)
            # print("make directory : " + fpath)


def fileSave(path, cont, opt, gzip_flag="n"):
    import gzip
    if gzip_flag == "gz":
        f = gzip.open(path, opt)
        f.write(cont)
        f.close()
    else:
        f = open(path, opt)
        f.write(cont)
        f.close


def fileOpen(path):
    f = open(path, "r")
    return f.read()


def is_exist(fpath):
    return os.path.exists(fpath)


def getNow():
    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    return s


def getNow2():
    now = time.localtime()
    s = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    return s


def get_url(url):
    if (sys.version_info > (3, 0)):
        response = urllib.request.urlopen(url)
        cont = response.read()
        return (cont.decode("UTF-8"))
    else:
        f = urllib.urlopen(url)
        return f.read()


def gzopen(fname):
    if fname.endswith(".gz"):
        import gzip
        f1 = gzip.GzipFile(fname, "r")
    else:
        f1 = open(fname)
    return f1


def getPath():
    return (os.path.join(bamsnap.__path__[0]))


def getTemplatePath(tempfile):
    return (os.path.join(bamsnap.__path__[0], 'templates', tempfile))

def getDataPath(datafile):
    return (os.path.join(bamsnap.__path__[0], 'data', datafile))

def load_json(jsonfile):
    ds = ""
    with open(jsonfile) as jfp:
        ds = json.load(jfp)
    return ds

def renderTemplate(templatefile, outfile, data={}):
    cont = fileOpen(getTemplatePath(templatefile))
    for k1 in data.keys():
        cont = cont.replace('##' + k1+ '##', data[k1])
    fileSave(outfile, cont, 'w')