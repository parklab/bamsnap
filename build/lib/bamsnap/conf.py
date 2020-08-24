from PIL import ImageColor


# version 0.02 (2020-02-38) : add gene view

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
COLOR['dA'] = ImageColor.getrgb("#078c07")
COLOR['dT'] = ImageColor.getrgb("#9c0808")
COLOR['dG'] = ImageColor.getrgb("#995508")
COLOR['dC'] = ImageColor.getrgb("#060680")
COLOR['dN'] = ImageColor.getrgb("#5c5959")
COLOR['MAPQ_0'] = ImageColor.getrgb("#EFEFEF")
COLOR['READ'] = ImageColor.getrgb("#c8c8c8")
COLOR['READPOS'] = (161, 156, 255, 255)
COLOR['READNEG'] = (255, 172, 156, 255)
COLOR['COVERAGE'] = ImageColor.getrgb("#b8b8b8")
COLOR['COVERAGE_BASE'] = (120, 120, 120, 255)
COLOR['NONPROPER_PAIR'] = ImageColor.getrgb("#343c44")
COLOR['DEL'] = ImageColor.getrgb("#000000")
COLOR['INS'] = ImageColor.getrgb("#7618dc")
COLOR['CENTER_LINE'] = ImageColor.getrgb("#999999")
COLOR['BG'] = ImageColor.getrgb("#FFFFFF")
COLOR['COORDINATE'] = (0, 0, 0, 255)
COLOR['SEPARATE'] = ImageColor.getrgb("#AAAAAA")
COLOR['LABEL'] = (0, 0, 0, 255)
COLOR['GENE_POS'] = ImageColor.getrgb("#6961ff")
# COLOR['GENE_NEG'] = ImageColor.getrgb("#e87489")
COLOR['GENE_NEG'] = (232, 116, 137, 255)
COLOR['GRID_COLOR'] = ImageColor.getrgb("#EEEEEE")


# A: "rgb(  0, 200,   0)",
# C: "rgb(  0,   0, 200)",
# T: "rgb(255,   0,   0)",
# G: "rgb(209, 113,   5)",

IMAGE_MARGIN_BOTTOM = 20

GENE_ANNOT_FILE  = "Homo_sapiens.#REFSEQVERSION#.bed.gz"

REFER_SEQ_VERSION = {'GRCh37': 'GRCh37', 'hg19':'GRCh37', 'GRCh38':'GRCh38', 'hg38':'GRCh38'}
