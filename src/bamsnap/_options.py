
import argparse
import sys
import os
from . import util

NOPRINTOPTLIST = ['log', 'chrom', 'g_epos', 'g_spos']


def postprocessing_option(opt):
    if 'out' in opt.keys() and (('logfile' not in opt.keys()) or (opt['logfile'] == "")):
        # opt['logfile'] = os.path.join(opt['out'] + '_bamsnap.log')
        opt['logfile'] = ""
    return opt


def loading_config(opt):
    for line in open(opt['conf']):
        line = line.strip()
        if len(line) > 0 and line[0] != "#":
            arr = line.split("=")
            k1 = arr[0].strip().lower()
            v1 = arr[1].strip()
            if len(k1) > 0:
                opt[k1] = v1
    return opt


def check_out_path(opt):
    if ('out' in opt.keys() and opt['out'] == ''):
        opt['out'] = './bamsnap_' + util.getNow2()
    if 'out' in opt.keys():
        util.check_dir(opt['out'])


def check_file(opt):
    flag = True
    if 'vcf' in opt.keys():
        pass
    if 'bam' in opt.keys():
        pass

    if not flag:
        # TODO: add check file
        pass
        # system.out()


def print_option(opt):
    global NOPRINTOPTLIST
    # print("=======option=======")
    # for k1 in sorted(opt.keys()):
    #     if k1 not in NOPRINTOPTLIST:
    #         if k1 == "poslist" and len(opt[k1]) >= 4:
    #             print('-' + k1 + " : " + str(len(opt[k1])) + " variants")
    #         else:
    #             print('-' + k1 + " : " + str(opt[k1]))
    # print("====================")
    pass


def set_pos_list(opt):
    ks = opt.keys()
    poslist = []
    if ('pos' in ks and len(opt['pos']) > 0):
        for opos in opt['pos']:
            if ':' in opos:
                p1 = {}
                arr = opos.split(':')
                p1['chrom'] = arr[0].strip()
                if '-' in arr[1]:
                    arr2 = arr[1].split('-')
                    p1['t_spos'] = int(arr2[0])
                    p1['t_epos'] = int(arr2[1]) + 1
                    if int(opt['margin']) > 0:
                        p1['g_spos'] = p1['t_spos'] - int(opt['margin'])
                        p1['g_epos'] = p1['t_epos'] + int(opt['margin'])
                else:  # SNV
                    p1['t_pos'] = int(arr[1])
                    p1['t_spos'] = int(arr[1])
                    p1['t_epos'] = int(arr[1]) + 1
                    p1['g_spos'] = p1['t_spos'] - int(opt['margin'])
                    p1['g_epos'] = p1['t_epos'] + int(opt['margin'])
                poslist.append(p1)

    if ('vcf' in ks and opt['vcf'] is not None):
        for line in util.gzopen(opt['vcf']):
            if opt['vcf'].endswith('.gz'):
                line = line.decode('UTF-8')
            if line[0] != '#':
                arr = line.split('\t')
                arr[-1] = arr[-1].strip()
                ref = arr[3].strip()
                alt = arr[4].strip()
                p1 = {}
                p1['chrom'] = arr[0].strip()
                p1['t_pos'] = int(arr[1])
                if len(ref) == 1 and len(alt) == 1:
                    p1['t_spos'] = int(arr[1])
                    p1['t_epos'] = int(arr[1]) + 1
                elif len(ref) > len(alt):
                    p1['t_spos'] = int(arr[1]) + 1
                    p1['t_epos'] = int(arr[1]) + len(ref)
                elif len(ref) < len(alt):
                    p1['t_spos'] = int(arr[1]) + 1
                    p1['t_epos'] = int(arr[1]) + len(alt)
                else:
                    p1['t_spos'] = int(arr[1]) + 1
                    p1['t_epos'] = int(arr[1]) + len(alt)

                p1['g_spos'] = p1['t_spos'] - int(opt['margin'])
                p1['g_epos'] = p1['t_epos'] + int(opt['margin'])

                if len(arr) >= 3:
                    p1['id'] = arr[2].strip()
                if len(arr) >= 4:
                    p1['ref'] = arr[3].strip()
                if len(arr) >= 5:
                    p1['alt'] = arr[4].strip()

                poslist.append(p1)
    if ('bed' in ks and opt['bed'] is not None):
        for line in util.gzopen(opt['bed']):
            if opt['bed'].endswith('.gz'):
                line = line.decode('UTF-8')
            if line[0] != '#':
                arr = line.split('\t')
                arr[-1] = arr[-1].strip()
                p1 = {}
                p1['chrom'] = arr[0].strip()
                p1['t_pos'] = int(arr[1])
                p1['t_spos'] = int(arr[1])
                p1['t_epos'] = int(arr[2]) + 1
                p1['g_spos'] = p1['t_spos'] - int(opt['margin'])
                p1['g_epos'] = p1['t_epos'] + int(opt['margin'])
                poslist.append(p1)

    if len(poslist) == 0:
        opt['log'].error('Please insert proper genomic position.')
        has_opt_error = True

    return poslist


def check_option(opt):
    ks = opt.keys()
    has_opt_error = False

    if ('out' in ks and opt['out'] == ''):
        opt['out'] = "bamsnap_"
        if opt['bam'] is not None:
            opt['out'] += opt['bam'].split('/')[-1]
        elif opt['bamlist'] is not None:
            opt['out'] += opt['bamlist'].split('/')[-1]
        opt['out'] += '_' + opt['pos'].replace(':', '_').replace('-', '_')

    if ('bam' not in ks or opt['bam'] is None) and ('bamlist' not in ks or opt['bamlist'] is None):
        opt['log'].error('Please insert bam file or bam file list with -bam or -bamlist option.')
        has_opt_error = True

    if ('pos' not in ks or opt['pos'] is None) and ('vcf' not in ks or opt['vcf'] is not None) and ('bed' not in ks or opt['bed'] is None):
        opt['log'].error('Please insert genomic position with -pos option.')
        has_opt_error = True
    else:
        opt['poslist'] = set_pos_list(opt)

    if has_opt_error:
        return


def convert_valuetype(typestr):
    rsttype = None
    if typestr is not None:
        if typestr == "int":
            rsttype = int
        if typestr == "float":
            rsttype = float
    return rsttype


def get_options():
    confjson = util.load_json(util.getDataPath('conf.json'))

    parser = argparse.ArgumentParser(usage='%(prog)s <sub-command> [options]',
                                     description='%(prog)s ver' + confjson['VERSION'] + " (" + confjson['VERSION_DATE'] + ")" + ': convert bam (or cram) to image')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ver' + confjson['VERSION'] + " (" + confjson['VERSION_DATE'] + ")")

    for a1 in confjson['options']:
        valuetype = convert_valuetype(a1['type'])
        if a1['action'] is not None:
            parser.add_argument('-' + a1['param'], default=a1['default'], help=a1['help'], action=a1['action'])
        else:
            parser.add_argument('-' + a1['param'], default=a1['default'],
                                help=a1['help'], nargs=a1['nargs'], type=valuetype)

    parser.add_argument('-silence', dest='silence', action="store_true", default=False, help='don\'t print any log.')

    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1][0] != '-'):
        sys.argv.append('-h')
    opt = vars(parser.parse_args())

    if 'conf' in opt.keys() and opt['conf'] is not None and util.is_exist(opt['conf']):
        opt = loading_config(opt)

    opt = postprocessing_option(opt)

    check_out_path(opt)
    check_option(opt)
    # check_file(opt)

    return opt
