
import argparse
import sys
import os
from . import conf
from . import util

NOPRINTOPTLIST = ['log', 'chrom', 'g_epos', 'g_spos']


def postprocessing_option(opt):
    if 'out' in opt.keys() and opt['out'] != "":
        util.check_dir(opt['out'] + '/test')
    if 'out' in opt.keys() and (('logfile' not in opt.keys()) or (opt['logfile'] == "")):
        opt['logfile'] = os.path.join(opt['out'], 'bamsnap.log')
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

# TODO:


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
    print("=======option=======")
    for k1 in sorted(opt.keys()):
        if k1 not in NOPRINTOPTLIST:
            print('-' + k1 + " : " + str(opt[k1]))
    print("====================")


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
                    p1['t_spos'] = int(arr2[0]) - 1
                    p1['t_epos'] = int(arr2[1])
                    if int(opt['margin']) > 0:
                        p1['g_spos'] = p1['t_spos'] - int(opt['margin'])
                        p1['g_epos'] = p1['t_epos'] + int(opt['margin'])
                else:  # SNV
                    p1['t_spos'] = int(arr[1]) - 1
                    p1['t_epos'] = int(arr[1])
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
                p1 = {}
                p1['chrom'] = arr[0].strip()
                p1['t_spos'] = int(arr[1]) - 1
                p1['t_epos'] = int(arr[1])
                p1['g_spos'] = p1['t_spos'] - int(opt['margin'])
                p1['g_epos'] = p1['t_epos'] + int(opt['margin'])
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
                p1['t_spos'] = int(arr[1]) - 1
                p1['t_epos'] = int(arr[2])
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


def get_options():
    parser = argparse.ArgumentParser(usage='%(prog)s <sub-command> [options]',
                                     description='%(prog)s ver' + conf.VERSION + " (" + conf.VERSION_DATE + ")" + ': convert bam to image')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ver' + conf.VERSION + " (" + conf.VERSION_DATE + ")")

    parser.add_argument('-bam', dest='bam', default=[], help='bam file', nargs="*")
    parser.add_argument('-bamlist', dest='bamlist', default=None, help='list file with bam file paths')
    parser.add_argument('-pos', dest='pos', default=[], nargs="*",
                        help='genomic position (ex. 1:816687-818057, 12:7462545)')
    parser.add_argument('-vcf', dest='vcf', default=None,
                        help='list file with genomic positions with VCF format')
    parser.add_argument('-bed', dest='bed', default=None,
                        help='list file with genomic positions with BED format')
    parser.add_argument('-out', dest='out', default='', help='title of output file')
    parser.add_argument('-out_type', dest='out_type',
                        choices=['png', 'jpg', 'image'], default='png', help='output file type')
    parser.add_argument('-conf', dest='conf', default="", help='configuration file')
    parser.add_argument('-ref', dest='ref', default="", help='Reference sequence fasta file (ex. hg19.fa)')
    parser.add_argument('-width', dest='width', default=1000, type=int, help='image size : width (unit:px)')
    parser.add_argument('-height', dest='height', default=None, help='image size : height (unit:px)')
    parser.add_argument('-read_thickness', dest='read_thickness', default=5, type=int, help='read width (unit:px)')
    parser.add_argument('-read_gap_h', dest='read_gap_h', default=2, type=int, help='read gap height (unit:px)')
    parser.add_argument('-read_gap_w', dest='read_gap_w', default=2, type=int, help='read gap width (unit:px)')
    parser.add_argument('-draw', dest='draw', default="coverage,heatmap,read",
                        help='plot (default: -draw coverage,heatmap,read )')
    parser.add_argument('-margin', dest='margin', default=200, type=int, help='genomic margin size')
    parser.add_argument('-center_line', dest='center_line', default=False, help='draw center line')
    parser.add_argument('-no_target_line', dest='no_target_line', default=False, help='do not draw target line')

    # coverage plot option
    # parser.add_argument('-draw_coverage_plot', dest='draw_coverage_plot',action="store_true", default=False, help='draw coverage plot')
    parser.add_argument('-coverage_height', dest='coverage_height', default=40, type=int, help='coverage plot height')
    parser.add_argument('-coverage_vaf', dest='coverage_vaf', default=10, type=float,
                        help='coverage variant allele fraction threshold (unit:%%)')

    # coverage heatmap height
    # parser.add_argument('-draw_heatmap', dest='draw_heatmap', action="store_true", default=False, help='draw heatmap')
    parser.add_argument('-heatmap_height', dest='heatmap_height', default=5, type=int, help='coverage heatmap height')

    # parser.add_argument('-draw_read', dest='draw_read_plot',action="store_true", default=False, help='draw read plot')
    parser.add_argument('-draw_gene', dest='draw_gene', default=True, help='draw gene structure')
    parser.add_argument('-merged_image', dest='merged_image', default=False, help='draw a merged plot')
    parser.add_argument('-colormap', dest='colormap', default=None, help='colormap file')
    parser.add_argument('-silence', dest='silence', action="store_true", default=False, help='don\'t print any log.')
    parser.add_argument('-debug', dest='debug', action="store_true", default=False, help='turn on the debugging mode')

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
