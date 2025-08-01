import os
import sys
import time
import json
from PIL import ImageColor

if sys.version_info > (3, 0):
    from html.parser import HTMLParser
    from urllib.parse import urlparse
    import urllib.request
else:
    from HTMLParser import HTMLParser
    import urlparse


def init_dict(dict1, key1, default_value=None):
    """
    Initialize a dictionary key with a default value if it doesn't exist.

    Args:
        dict1 (dict): Dictionary to initialize
        key1: Key to check/initialize
        default_value: Value to set if key doesn't exist (default: {})

    Returns:
        dict: The dictionary (for method chaining)

    Example:
        >>> d = {}
        >>> init_dict(d, 'key1')
        >>> print(d)  # {'key1': {}}

        >>> init_dict(d, 'key2', [])
        >>> print(d)  # {'key1': {}, 'key2': []}
    """
    if default_value is None:
        default_value = {}

    if key1 not in dict1:
        dict1[key1] = default_value

    return dict1


def add_dict_value(dict1, key1, add_value=1):
    """
    Add a value to a dictionary key, initializing the key if it doesn't exist.

    Args:
        dict1 (dict): Dictionary to modify
        key1: Key to add value to
        add_value (int/float): Value to add (default: 1)

    Returns:
        dict: The modified dictionary (for method chaining)

    Example:
        >>> d = {}
        >>> add_dict_value(d, 'count', 5)
        >>> print(d)  # {'count': 5}

        >>> add_dict_value(d, 'count', 3)
        >>> print(d)  # {'count': 8}

        >>> add_dict_value(d, 'total')  # Defaults to adding 1
        >>> print(d)  # {'count': 8, 'total': 1}
    """
    if key1 in dict1:
        dict1[key1] += add_value
    else:
        dict1[key1] = add_value

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
        if s1 != "":
            try:
                intlist.append(int(s1))
            except ValueError:
                pass
    return intlist


def comma(value):
    return "{:,}".format(value)


def mkDir(dpath):
    """
    Create a directory and all necessary parent directories.
    
    Args:
        dpath (str): Directory path to create
        
    Note:
        This function will create all parent directories if they don't exist.
        It handles the case where the directory already exists gracefully.
    """
    if not os.path.exists(dpath):
        os.makedirs(dpath, exist_ok=True)

def decodeb(bstr):
    if type(bstr) == type(b"a"):
        rst = bstr.decode("UTF-8")
    else:
        rst = bstr
    return rst


def check_dir(fname):
    """
    Create parent directories for a given file path if they don't exist.
    
    Args:
        fname (str): File path for which to create parent directories
    """
    if not fname:
        return
    
    # Get the directory part of the path
    dir_path = os.path.dirname(os.path.abspath(fname))
    
    # Create the directory if it doesn't exist
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")



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


def file_exist(fpath):
    """
    Check if a file or directory exists.

    Args:
        fpath (str or Path): Path to check for existence

    Returns:
        bool: True if path exists, False otherwise

    Note:
        This function handles None input gracefully and works with both
        string paths and pathlib.Path objects.
    """
    if fpath is None:
        return False

    try:
        return os.path.exists(fpath)
    except (TypeError, OSError):
        return False


def getNow():
    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (
        now.tm_year,
        now.tm_mon,
        now.tm_mday,
        now.tm_hour,
        now.tm_min,
        now.tm_sec,
    )
    return s


def getNow2():
    now = time.localtime()
    s = "%04d%02d%02d%02d%02d%02d" % (
        now.tm_year,
        now.tm_mon,
        now.tm_mday,
        now.tm_hour,
        now.tm_min,
        now.tm_sec,
    )
    return s


def get_url(url):
    if sys.version_info > (3, 0):
        response = urllib.request.urlopen(url)
        cont = response.read()
        return cont.decode("UTF-8")
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
    return os.path.abspath(__file__)


def getTemplatePath(tempfile):
    parent_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(parent_path, "templates", tempfile)


def getDataPath(datafile):
    parent_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(parent_path, "data", datafile)


def load_json(jsonfile):
    ds = ""
    with open(jsonfile) as jfp:
        ds = json.load(jfp)
    return ds


def renderTemplate(templatefile, outfile, data={}):
    cont = fileOpen(getTemplatePath(templatefile))
    for k1 in data.keys():
        cont = cont.replace("##" + k1 + "##", data[k1])
    fileSave(outfile, cont, "w")


def is_file_path(path):
    """
    Determine if a given path is intended to be a file path or directory path,
    even if the file or directory does not exist yet.
    
    Args:
        path (str): Path to analyze
        
    Returns:
        bool: True if path appears to be a file path, False if directory path
        
    Example:
        >>> is_file_path("/path/to/file.txt")
        True
        >>> is_file_path("/path/to/directory/")
        False
        >>> is_file_path("/path/to/directory")
        False  # Ambiguous case - treated as directory
        >>> is_file_path("output.png")
        True
    """
    if not path:
        return False
    
    # Normalize path separators
    path = os.path.normpath(path)
    
    # If path exists, use actual filesystem info
    if os.path.exists(path):
        return os.path.isfile(path)
    
    # If path ends with separator, it's definitely a directory
    if path.endswith(os.sep) or path.endswith('/'):
        return False
    
    # Get the last component of the path
    basename = os.path.basename(path)
    
    # If basename is empty (path ends with separator), it's a directory
    if not basename:
        return False
    
    # If basename has a file extension, it's likely a file
    if '.' in basename and not basename.startswith('.'):
        # Check if it's a reasonable file extension (not just dots)
        name, ext = os.path.splitext(basename)
        if name and ext and len(ext) <= 10:  # Reasonable extension length
            return True
    
    # Check for common file patterns
    file_indicators = [
        basename.startswith('.') and '.' in basename[1:],  # Hidden files with extensions
        any(basename.endswith(ext) for ext in ['.txt', '.log', '.dat', '.tmp']),  # Common extensions
    ]
    
    if any(file_indicators):
        return True
    
    # Check for common directory patterns
    directory_indicators = [
        basename in ['bin', 'lib', 'src', 'data', 'output', 'temp', 'tmp'],
        basename.endswith('_dir') or basename.endswith('_directory'),
        basename.startswith('dir_'),
    ]
    
    if any(directory_indicators):
        return False
    
    # Default: treat ambiguous cases as directories for safety
    # This prevents accidentally creating files when directories were intended
    return False

