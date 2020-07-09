import logging

_loggers = {}
_silence_flag = None
_debug_flag = None
_logfile = ""


def get_logger(silence=None, debug=None, logfile=""):
    global _loggers, _silence_flag, _debug_flag, _logfile

    name = "bamsnap"
    # print (debug)
    if name not in _loggers:
        _log = logging.getLogger(name)

        if silence is not None:
            _silence_flag = silence
        elif _silence_flag is None:
            _silence_flag = False

        if debug is not None:
            _debug_flag = debug
        elif _debug_flag is None:
            _debug_flag = False

        if _debug_flag:
            _log.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(module)s %(lineno)d: [%(levelname)s] %(message)s')
        else:
            _log.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s : [%(levelname)s] %(message)s')

        if not _silence_flag:
            sh = logging.StreamHandler()
            sh.setFormatter(formatter)
            _log.addHandler(sh)

        if logfile != "":
            _logfile = logfile
            fh = logging.FileHandler(_logfile)
            fh.setFormatter(formatter)
            _log.addHandler(fh)

        _loggers[name] = _log
    return _loggers[name]
