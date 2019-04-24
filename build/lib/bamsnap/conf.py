from PIL import ImageColor

TITLE = 'BAMSNAP'
VERSION = "0.01"
VERSION_DATE = "2019-04-05"
PROG = "bamsnap"

# REF_SEQ_FASTA = {}
# REF_SEQ_FASTA['GRCh37']  = '/home/mk446/BiO/Install/GATK-bundle/2.8/b37/human_g1k_v37_decoy.fasta'
# REF_SEQ_FASTA['GRCh37d5'] = '/home/mk446/BiO/Install/GATK-bundle/2.8/b37/human_g1k_v37_decoy.fasta'
# REF_SEQ_FASTA['hg19']    = "/home/mk446/BiO/Install/GATK-bundle/2.8/hg19/ucsc.hg19.fasta"
# REF_SEQ_FASTA['hg38']    = "/n/data1/hms/dbmi/park/SOFTWARE/REFERENCE/hg38.ucsc/ucsc.hg38.sorted.fa"
# REF_SEQ_FASTA['hg38d']   = "/home/mk446/BiO/Install/GATK-bundle/2.8/hg38/Homo_sapiens_assembly38.fasta"
# REF_SEQ_FASTA['GRCh38']  = "/home/mk446/BiO/Install/GATK-bundle/Homo_sapiens.GRCh38.dna.primary_assembly.reorder.fasta"   #### without decoy
# REF_SEQ_FASTA['GRCh38d'] = "/home/mk446/BiO/Install/GATK-bundle/2.8/b38/GRCh38_full_analysis_set_plus_decoy_hla.fa"   #### with decoy

COLOR = {}
COLOR['cov'] = ImageColor.getrgb("#AAAAAA")
COLOR['A'] = ImageColor.getrgb("#00ff00")
COLOR['T'] = ImageColor.getrgb("#ff0000")
COLOR['G'] = ImageColor.getrgb("#d17105")
COLOR['C'] = ImageColor.getrgb("#0000ff")
COLOR['N'] = ImageColor.getrgb("#AAAAAA")
COLOR['wA'] = ImageColor.getrgb("#64E464")
COLOR['wG'] = ImageColor.getrgb("#CAB7A1")
COLOR['wC'] = ImageColor.getrgb("#8C8CD9")
COLOR['wT'] = ImageColor.getrgb("#DE7878")
COLOR['wN'] = ImageColor.getrgb("#AAAAAA")
COLOR['MAPQ_0'] = ImageColor.getrgb("#EFEFEF")
COLOR['READ'] = ImageColor.getrgb("#c8c8c8")
COLOR['COVERAGE'] = ImageColor.getrgb("#b8b8b8")
COLOR['NONPROPER_PAIR'] = ImageColor.getrgb("#343c44")
COLOR['DEL'] = ImageColor.getrgb("#000000")
COLOR['INS'] = ImageColor.getrgb("#7618dc")
COLOR['CENTER_LINE'] = (0,0,0,110)
COLOR['BG'] = ImageColor.getrgb("#FFFFFF")
# A: "rgb(  0, 200,   0)",
# C: "rgb(  0,   0, 200)",
# T: "rgb(255,   0,   0)",
# G: "rgb(209, 113,   5)",
