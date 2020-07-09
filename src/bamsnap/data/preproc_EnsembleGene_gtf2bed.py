#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

def fileSave (path, cont, opt, gzip_flag = "n"):
    if gzip_flag == "gz":
        import gzip
        f = gzip.open(path, opt)
        f.write(cont)
        f.close()
    else:
        f = open (path, opt)
        f.write(cont)
        f.close

def run_cmd(scmd, flag=False):
    if flag:
        print (scmd)
    rst = os.popen(scmd)
    rst_cont = rst.read()
    return rst_cont

def gzopen(fname):
    if fname.endswith(".gz"):
        import gzip
        f1 = gzip.GzipFile(fname, "r")
    else:
        f1 = open(fname)
    return f1

def gv(d1, k1):
    v1 = ''
    try:
        v1 = d1[k1]
    except KeyError:
        pass
    return v1

def count_no_fields(cnt, fieldname, value):
    try:
        tmp = cnt[fieldname]
    except KeyError:
        cnt[fieldname] = {}

    try:
        cnt[fieldname][value] += 1
    except KeyError:
        cnt[fieldname][value] = 1
    return cnt


fieldlist = []
fieldlist.append('gene_id')
fieldlist.append('gene_version')
fieldlist.append('gene_name')
fieldlist.append('gene_source')
fieldlist.append('gene_biotype')
fieldlist.append('transcript_id')
fieldlist.append('transcript_version')
fieldlist.append('transcript_name')
fieldlist.append('transcript_source')
fieldlist.append('transcript_biotype')
fieldlist.append('transcript_support_level')
fieldlist.append('tag')
fieldlist.append('exon_id')
fieldlist.append('exon_number')
fieldlist.append('exon_version')
fieldlist.append('protein_id')
fieldlist.append('protein_version')
fieldlist.append('ccds_id')

fieldlist_compress = []
fieldlist_compress.append('gene_id')
fieldlist_compress.append('gene_name')
fieldlist_compress.append('gene_biotype')
fieldlist_compress.append('transcript_id')
fieldlist_compress.append('transcript_biotype')
fieldlist_compress.append('transcript_spos')
fieldlist_compress.append('transcript_epos')

LINETYPE = []
# LINETYPE.append('gene')
# LINETYPE.append('transcript')
LINETYPE.append('exon')
LINETYPE.append('CDS')
LINETYPE.append('start_codon')
LINETYPE.append('stop_codon')
LINETYPE.append('five_prime_utr')
LINETYPE.append('three_prime_utr')
LINETYPE.append('Selenocysteine')



def save_compressed_bed(f, d):
    cont = []
    cont.append(d['chrom'])
    cont.append(d['spos'])
    cont.append(d['epos'])
    cont.append(d['strand'])
    cont.append(d['gene_id'])
    cont.append(d['gene_name'])
    cont.append(d['gene_biotype'])
    trlist = list(d['transcript'].keys())
    cont.append('|'.join(trlist))

    transcript_biotype_list = []
    transcript_spos_list = []
    transcript_epos_list = []
    ltype_list = {}
    for ltype in LINETYPE:
        ltype_list[ltype+'_spos'] = []
        ltype_list[ltype+'_epos'] = []

    for tid in trlist:
        t1 = d['transcript'][tid]    
        transcript_biotype_list.append(t1['transcript_biotype'])
        transcript_spos_list.append(t1['spos'])
        transcript_epos_list.append(t1['epos'])

        for ltype in LINETYPE:
            sposlist = []
            eposlist = []
            if ltype in t1.keys():
                for a1 in t1[ltype]:
                    sposlist.append(a1['spos'])
                    eposlist.append(a1['epos'])
            ltype_list[ltype+'_spos'].append(','.join(sposlist))
            ltype_list[ltype+'_epos'].append(','.join(eposlist))

    cont.append('|'.join(transcript_biotype_list))
    cont.append('|'.join(transcript_spos_list))
    cont.append('|'.join(transcript_epos_list))

    for ltype in LINETYPE:
        cont.append('|'.join(ltype_list[ltype+'_spos']))
        cont.append('|'.join(ltype_list[ltype+'_epos']))

    # if d['spos'] == '17368':
    #     print(cont)
    f.write('\t'.join(cont) + '\n')


def convert_ensemblgene_gtf2bed(gtf, bed, gtftypes, biotypes=[], outtype="all"):
    global fieldlist

    print("Processing....",gtf)

    f = open(bed, 'w')
    if outtype == "all":
        cont = ["#CHROM", "SPOS", "EPOS", "type" ,"strand"]
        cont.extend(fieldlist)
    else:
        cont = ["#CHROM", "SPOS", "EPOS" ,"strand"]
        cont.extend(fieldlist_compress)
        for ltype in LINETYPE:
            cont.append(ltype + '_spos')
            cont.append(ltype + '_epos')

    f.write('\t'.join(cont) + '\n')
    i = 0
    cnt = {}

    # print(len(fieldlist))
    # d = {'transcript':[]}
    d = {}

    for line in gzopen(gtf):
        line = line.decode('UTF-8')
        if line[0] != '#':
            arr = line.split('\t')
            arr[-1] = arr[-1].strip()

            gtftype = arr[2]

            if (gtftypes[0] == "alltype") or (gtftype in gtftypes):
                i += 1
                if arr[0] == "MT":
                    arr[0] = "M"
                
                cnt = count_no_fields(cnt, 'chrom', arr[0])
                m = {}
                for f1 in arr[-1].strip().split(';'):
                    arr2 = f1.strip().split(' ')
                    fieldname = arr2[0].strip()
                    value = ' '.join(arr2[1:]).replace('"','')
                    m[fieldname] = value

                    if fieldname not in ['gene_id','gene_name']:
                        cnt = count_no_fields(cnt, fieldname, value)

                ltype = arr[2]
                chrom = arr[0]
                spos = str(int(arr[3])-1)
                epos = arr[4]
                strand = arr[6]
                m['ltype'] = ltype
                m['chrom'] = chrom
                m['spos'] = spos
                m['epos'] = epos
                m['strand'] = strand

                cnt = count_no_fields(cnt, 'linetype', ltype)
                if ltype == "gene":
                    if len(d.keys()) > 0:
                        if outtype != "all":
                            # print(d['strand'])
                            save_compressed_bed(f, d)
                    
                    d = {}
                    for k1 in m.keys():
                        d[k1] = m[k1]
                    d['transcript'] = {}

                elif ltype == "transcript":
                    d['transcript'][m['transcript_id']] = m
                else:
                    try:
                        d['transcript'][m['transcript_id']][ltype].append(m)
                    except KeyError:
                        d['transcript'][m['transcript_id']][ltype] = [m]
                    
            
                if (len(biotypes) == 0) or (m['gene_biotype'] in biotypes):
                    cont = [arr[0], str(int(arr[3])-1), arr[4], arr[2] , arr[6]]
                    for f1 in fieldlist:
                        cont.append(gv(m,f1))
                    if outtype == "all":
                        f.write('\t'.join(cont) + '\n')
                

                # break
                if i % 10000 == 0:
                    print(i, arr[:4])
                    # break
    
    if outtype != "all" and len(d.keys()) > 0:
        save_compressed_bed(f, d)
    f.close()
    

    cont = ''
    for k1 in cnt.keys():
        # print(k1)
        cont += k1 + '\n'
        for k2 in cnt[k1].keys():
            cont += '\t' + k2 + '\t' + str(cnt[k1][k2]) + '\n'
            # print('\t',k2, cnt[k1][k2])
    fileSave(bed + '.stat', cont, 'w')
    
    run_cmd("bgzip -c "+bed+" > "+bed+".gz", True)
    run_cmd("tabix -f -p bed "+bed+".gz", True)
    # sortbed = bed.replace('.bed','') + ".sorted.bed"
    # run_cmd("vcf-sort -c "+bed+" > " + sortbed, True)
    # run_cmd("bgzip -c "+sortbed+" > "+sortbed+".gz", True)
    # run_cmd("tabix -f -p bed "+sortbed+".gz", True)


if __name__ == "__main__":
    print("# USAGE: python preproc_EnsembleGene_gtf2bed.py Homo_sapiens.GRCh38.99.gtf.gz")
    gtf = sys.argv[1]
    out = gtf.replace('.gtf.gz', '.bed')
    # convert_ensemblgene_gtf2bed(gtf, path + "Homo_sapiens.GRCh38.99.alltype.bed", ["alltype"])
    convert_ensemblgene_gtf2bed(gtf, out , ["alltype"], ['protein_coding','miRNA','polymorphic_pseudogene'], "compressed")
    # convert_ensemblgene_gtf2bed(gtf, out , ["alltype"], ['protein_coding','miRNA','polymorphic_pseudogene'], "all")

