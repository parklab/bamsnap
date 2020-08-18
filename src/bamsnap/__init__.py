from ._logging import get_logger
from ._options import get_options, print_option
from .bamsnap import BamSnap
from .web import runserver


def cli():
    opt = get_options()
    if not opt['silence']:
        print_option(opt)
    if opt['viewer']:
    	runserver(opt)
    else:
	    opt['log'] = get_logger(silence=opt['silence'], debug=opt['debug'], logfile=opt['logfile'])
	    bs = BamSnap(opt)
	    bs.run()
