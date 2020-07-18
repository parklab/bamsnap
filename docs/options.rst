Optional arguments
==================

* ``-h``, ``--help`` : show this help message and exit
* ``-v``, ``--version`` : show program's version number and exit
* ``-silence`` : don't print any log.
* ``-debug`` : turn on debugging mode

**Input files**

* ``-bam``: `bam file(s) <input.html#bam-file-bam>`_
* ``-bamlist`` : `list file with bam file paths <input.html#bam-list-file-bamlist>`_
  
  * ``-title`` : `title (name) of bam file(s) <input.html#title-of-bam-file-s-title>`_
  * ``-no_title`` : `do not draw label (title) (default: false) <input.html#title-of-bam-file-s-title>`_
  * ``-title_fontsize`` : font size of title

* ``-pos`` : `genomic position <input.html#single-position-pos>`_
* ``-vcf`` : `list file with genomic positions with VCF format <input.html#vcf-file-vcf>`_
* ``-bed`` : `list file with genomic positions with BED format <input.html#bed-file-bed>`_
* ``-ref`` : `Reference sequence fasta file <input.html#fasta-file-ref>`_

  * ``-ref_index_rebuild`` : `if you want to rebuild fasta index file (.fai), when it is older than the fasta file. (default: false) <input.html#fasta-file-ref>`_
  * ``-refversion [hg38, hg19]`` : `Reference version (default: hg38) <input.html#reference-sequence-file>`_

* ``-conf`` : configuration file

**Output file**

* ``-out`` : output file name or title of output file

  * ``-imagetype [png, jpg]`` : output file type (default:png)
  * ``-save_image_only`` : save image only (default:false)
  * ``-image_dir_name`` : image directory name
  * ``-zipout`` : make a single zip file

**Plot options**

* ``-separator_height`` : separator's height
* ``-draw`` : plot (default: -draw coordinates bamplot base gene)
* ``-bamplot`` : plot (default: -bamplot coverage base read)
* ``-width`` : image file size : width (unit:px)
* ``-height`` : image file size : height (unit:px)
* ``-bgcolor`` : background color
* ``-plot_margin_top`` : top margin size of plot
* ``-plot_margin_bottom`` : bottom margin size of plot
* ``-plot_margin_left`` : left margin size of plot
* ``-plot_margin_right`` : right margin size of plot
* ``-border`` : draw border in plot
* ``-separated_bam`` : draw a plot for each bam

**Read alignment plot**

* ``-read_thickness`` : read thickness (unit:px)
* ``-read_gap_height`` : read gap height (unit:px)
* ``-read_gap_width`` : read gap width (unit:px)
* ``-read_bgcolor`` : read background color
* ``-read_color`` : read color
* ``-read_pos_color`` : positive strand read color
* ``-read_neg_color`` : negative strand read color
* ``-read_group`` : read group
* ``-margin`` : genomic margin size
* ``-center_line`` : draw center line
* ``-no_target_line`` : do not draw target line

**Base plot**

* ``-base_fontsize`` : font size of base plot
* ``-base_height`` : base plot height
* ``-base_margin_top`` : top margin size of base plot
* ``-base_margin_bottom`` : bottom margin size of base plot

**Coverage plot**

* ``-coverage_height`` : coverage plot height
* ``-coverage_fontsize`` : coverage font size
* ``-coverage_vaf`` : coverage variant allele fraction threshold (default: 0.2)
* ``-coverage_color`` : coverage color
* ``-coverage_bgcolor`` : coverage plot background color

**Heat map**

* ``-heatmap_height`` : coverage heatmap height
* ``-heatmap_bgcolor`` : coverage heatmap plot background color
  
**Gene plot**

* ``-gene_height`` : gene plot height
* ``-gene_fontsize`` : font size of gene plot
* ``-gene_pos_color`` : positive strand color
* ``-gene_neg_color`` : negative strand color

**Coordinates plot**

* ``-coordinates_height`` : coordinate height
* ``-coordinates_fontsize`` : coordinate font size
* ``-coordinates_axisloc`` : coordinate axis location
* ``-coordinates_bgcolor`` : coordinate background color
* ``-coordinates_labelcolor`` : coordinate label color



  
  
  