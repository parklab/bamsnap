from ._logging import get_logger
from ._options import get_options, print_option
from .bamsnap import BamSnap


def cli():
    opt = get_options()
    if not opt['silence']:
        print_option(opt)
    opt['log'] = get_logger(silence=opt['silence'], debug=opt['debug'], logfile=opt['logfile'])
    bs = BamSnap(opt)
    bs.run()
