Optional arguments
==================

* ``-h``, ``--help`` : show this help message and exit
* ``-v``, ``--version`` : show program's version number and exit
* ``-silence`` : don't print any log.
* ``-debug`` : turn on debugging mode
* ``-process`` (default=1) : number of process for multi-processing

**Input files**

* ``-bam``: `bam file(s) <input.html#bam-file-bam>`_
* ``-bamlist`` : `list file with bam file paths <input.html#bam-list-file-bamlist>`_
  
  * ``-title`` : `title (name) of bam file(s) <input.html#title-of-bam-file-s-title>`_
  * ``-no_title`` : `do not draw label (title) (default: false) <input.html#title-of-bam-file-s-title>`_
  * ``-title_fontsize`` (default=18) : font size of title

* ``-pos`` : `genomic position <input.html#single-position-pos>`_
* ``-vcf`` : `list file with genomic positions with VCF format <input.html#vcf-file-vcf>`_
* ``-bed`` : `list file with genomic positions with BED format <input.html#bed-file-bed>`_
* ``-ref`` : `Reference sequence fasta file <input.html#fasta-file-ref>`_

  * ``-ref_index_rebuild`` (default=false) : `if you want to rebuild fasta index file (.fai), when it is older than the fasta file. <input.html#fasta-file-ref>`_
  * ``-refversion [hg38, hg19]`` (default=hg38) : `Reference version <input.html#reference-sequence-file>`_

* ``-conf`` : configuration file

**Output file**

* ``-out`` : `output file name or title of output file <output.html>`_

  * ``-imagetype [png, jpg]`` (default=png) : `output file type <output.html#image-file-png-jpg>`_
  * ``-save_image_only`` (default=false) : `save image only <output.html#image-file-png-jpg>`_
  * ``-image_dir_name`` : `image directory name <output.html#image-file-png-jpg>`_
  * ``-zipout`` (default=false) : `make a single zip file <output.html#compressed-file-zipout>`_
  * ``-separated_bam`` : `draw a plot for each bam <output.html#image-file-png-jpg>`_

**Plot options**

* ``-draw`` (default=coordinates bamplot base gene) : `track composition <plot.html#plot-composition>`_
* ``-bamplot`` (default=coverage base read) : `track composition in bamplot  <plot.html#plot-composition>`_
* ``-width`` (default=1000): `image width (unit:px) <plot.html#plot-layout-options>`_
* ``-height`` : `image height (unit:px) <plot.html#plot-layout-options>`_
* ``-bgcolor`` : `background color <plot.html#plot-layout-options>`_
* ``-plot_margin_top`` : `top margin size of plot (default: 20) <plot.html#plot-layout-options>`_
* ``-plot_margin_bottom`` : `bottom margin size of plot <plot.html#plot-layout-options>`_
* ``-plot_margin_left`` : `left margin size of plot <plot.html#plot-layout-options>`_
* ``-plot_margin_right`` : `right margin size of plot <plot.html#plot-layout-options>`_
* ``-border`` : `draw border in plot <plot.html#plot-layout-options>`_
* ``-separator_height`` (default=30): `separator's height <plot.html#plot-layout-options>`_


**Read alignment track**

* ``-read_thickness`` (default=5) : `read thickness (unit:px) <read_plot.html>`_
* ``-read_gap_height`` (default=50) : `read gap height (unit:px) <read_plot.html>`_
* ``-read_gap_width`` : `read gap width (unit:px) <read_plot.html>`_
* ``-read_bgcolor`` : `read background color <read_plot.html>`_
* ``-read_color`` : `read color <read_plot.html>`_
* ``-margin`` (default=50) : `genomic margin size <read_plot.html>`_
* ``-center_line`` : `draw center line <read_plot.html>`_
* ``-no_target_line`` : `do not draw target line <read_plot.html>`_
* ``-read_group`` : `read color <read_plot.html>`_
* ``-read_pos_color`` : `positive strand read color <read_plot.html>`_
* ``-read_neg_color`` : `negative strand read color <read_plot.html>`_

**Base track**

* ``-base_fontsize`` (default=9) : `font size of base <base_plot.html>`_
* ``-base_height`` (default=30) : `base track height <base_plot.html>`_
* ``-base_margin_top`` (default=0) : `top margin size of base track <base_plot.html>`_
* ``-base_margin_bottom`` (default=0) : `bottom margin size of base track <base_plot.html>`_

**Coverage track**

* ``-coverage_height`` (default=40) : `coverage track height <coverage_plot.html>`_
* ``-coverage_fontsize`` (default=9) : `coverage font size <coverage_plot.html>`_
* ``-coverage_vaf`` (default=0.2) : `coverage variant allele fraction threshold <coverage_plot.html>`_
* ``-coverage_color`` (default=C8C8C8) : `coverage color <coverage_plot.html>`_
* ``-coverage_bgcolor`` (default=FFFFFF) : `coverage track background color <coverage_plot.html>`_

**Heatmap track**

* ``-heatmap_height`` (default=5) : `coverage heatmap height <heatmap.html>`_
* ``-heatmap_bgcolor`` (default=FFFFFF) : `coverage heatmap track background color <heatmap.html>`_
  
**Gene track**

* ``-gene_height`` (default=50) : `gene track height <gene_plot.html>`_
* ``-gene_fontsize`` (default=10) : `font size of gene track <gene_plot.html>`_
* ``-gene_pos_color`` (default=FFAC9C) : `positive strand color <gene_plot.html>`_
* ``-gene_neg_color`` (default=A19CFF) : `negative strand color <gene_plot.html>`_

**Coordinates track**

* ``-coordinates_height`` (default=20) : `coordinates height <coordinates_plot.html>`_
* ``-coordinates_fontsize`` (default=12) : `coordinates font size <coordinates_plot.html>`_
* ``-coordinates_axisloc [top, bottom, middle]`` (default=bottom) : `coordinates axis location <coordinates_plot.html>`_
* ``-coordinates_bgcolor`` (default=FFFFFF) : `coordinates background color <coordinates_plot.html>`_
* ``-coordinates_labelcolor`` (default=000000) : `coordinates label color <coordinates_plot.html>`_



  
  
  