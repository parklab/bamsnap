Options
=======


.. code:: console

  optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -bam [BAM [BAM ...]]  bam file(s)
  -bamlist BAMLIST      list file with bam file paths
  -title [TITLE [TITLE ...]]
                        title (name) of bam file(s)
  -pos [POS [POS ...]]  genomic position (ex. 1:816687-818057, 12:7462545)
  -vcf VCF              list file with genomic positions with VCF format
  -bed BED              list file with genomic positions with BED format
  -out OUT              output file or title of output file
  -imagetype IMAGETYPE  output file type
  -conf CONF            configuration file
  -ref REF              Reference sequence fasta file (ex. hg19.fa)
  -refversion REFVERSION
                        Reference version (default: hg38)
  -save_image_only      save image only
  -image_dir_name IMAGE_DIR_NAME
                        image directory name
  -zipout               make a single zip file
  -separator_height SEPARATOR_HEIGHT
                        separator's height
  -draw [DRAW [DRAW ...]]
                        plot (default: -draw coordinates bamplot base gene)
  -bamplot [BAMPLOT [BAMPLOT ...]]
                        plot (default: -bamplot coverage base read)
  -width WIDTH          image file size : width (unit:px)
  -height HEIGHT        image file size : height (unit:px)
  -bgcolor BGCOLOR      background color
  -plot_margin_top PLOT_MARGIN_TOP
                        top margin size of plot
  -plot_margin_bottom PLOT_MARGIN_BOTTOM
                        bottom margin size of plot
  -plot_margin_left PLOT_MARGIN_LEFT
                        left margin size of plot
  -plot_margin_right PLOT_MARGIN_RIGHT
                        right margin size of plot
  -border               draw border in plot
  -read_thickness READ_THICKNESS
                        read thickness (unit:px)
  -read_gap_height READ_GAP_HEIGHT
                        read gap height (unit:px)
  -read_gap_width READ_GAP_WIDTH
                        read gap width (unit:px)
  -read_bgcolor READ_BGCOLOR
                        read background color
  -read_color READ_COLOR
                        read color
  -read_pos_color READ_POS_COLOR
                        positive strand read color
  -read_neg_color READ_NEG_COLOR
                        negative strand read color
  -read_group READ_GROUP
                        read group
  -margin MARGIN        genomic margin size
  -center_line          draw center line
  -no_target_line       do not draw target line
  -base_fontsize BASE_FONTSIZE
                        font size of base plot
  -base_height BASE_HEIGHT
                        base plot height
  -base_margin_top BASE_MARGIN_TOP
                        top margin size of base plot
  -base_margin_bottom BASE_MARGIN_BOTTOM
                        bottom margin size of base plot
  -coverage_height COVERAGE_HEIGHT
                        coverage plot height
  -coverage_fontsize COVERAGE_FONTSIZE
                        coverage font size
  -coverage_vaf COVERAGE_VAF
                        coverage variant allele fraction threshold (default:
                        0.2)
  -coverage_color COVERAGE_COLOR
                        coverage color
  -coverage_bgcolor COVERAGE_BGCOLOR
                        coverage plot background color
  -heatmap_height HEATMAP_HEIGHT
                        coverage heatmap height
  -heatmap_bgcolor HEATMAP_BGCOLOR
                        coverage heatmap plot background color
  -no_title             do not draw label.
  -gene_height GENE_HEIGHT
                        gene plot height
  -gene_fontsize GENE_FONTSIZE
                        font size of gene plot
  -gene_pos_color GENE_POS_COLOR
                        positive strand color
  -gene_neg_color GENE_NEG_COLOR
                        negative strand color
  -coordinates_height COORDINATES_HEIGHT
                        coordinate height
  -coordinates_fontsize COORDINATES_FONTSIZE
                        coordinate font size
  -coordinates_axisloc COORDINATES_AXISLOC
                        coordinate axis location
  -coordinates_bgcolor COORDINATES_BGCOLOR
                        coordinate background color
  -coordinates_labelcolor COORDINATES_LABELCOLOR
                        coordinate label color
  -separated_bam        draw a plot for each bam
  -title_fontsize TITLE_FONTSIZE
                        font size of title
  -debug                turn on the debugging mode
  -silence              don't print any log
