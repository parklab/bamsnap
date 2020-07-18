Input files
===========


Alignment file
--------------

**BamSnap** supports only sorted and indexed bam file. The bam index file (``.bam.bai`` or ``.bai``) is required in same location. 


BAM file (``-bam``)
^^^^^^^^^^^^^^^^^^^

For a single bam file or multiple bam files, you can add bam file paths with ``-bam`` argument.

.. code:: console

    $ bamsnap -bam ./data/NA12878.bam
    $ bamsnap -bam ./data/NA12878.bam ./data/NA12877.bam ./data/NA12879.bam


Title of bam file(s) (``-title``)
:::::::::::::::::::::::::::::::::

If you want to add another label for each bam plot, you can add titles with ``-title`` argument.

.. code:: console

    $ bamsnap -bam ./data/NA12879.bam -title NA12879
    $ bamsnap -bam ./data/NA12879.bam -title "NA12879  (Daughter)"
    $ bamsnap -bam ./data/NA12878.bam ./data/NA12877.bam ./data/NA12879.bam \
      -title "NA12877 (Father)" "NA12878 (Mother)" "NA12879 (Daughter)" 

.. image:: img/pic_title1.png
   :width: 300 px


If you don't add ``-title``, the title can be bam file name automatically. 

.. image:: img/pic_title2.png
   :width: 300 px

If you don't want to add label, you can use ``-no_title`` option.


.. code:: console

    $ bamsnap -bam ./data/NA12879.bam -no_title


.. image:: img/pic_title3.png
   :width: 300 px

BAM list file (``-bamlist``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: console

    $ bamsnap -bamlist ./data/NATRIO_bamlist.txt


BAM list file includes two columns of bam file path and its title. The columns are separated by tab.

.. code:: bash

  # example of bamlist file
  ./data/NA12878.bam  NA12878 (F)
  ./data/NA12877.bam  NA12877 (M)
  ./data/NA12879.bam  NA12879 (D)

Or, you can use just one columns (bam file path) without its title. In this case, title can be bam file name.

.. code:: bash

  # example of bamlist file
  ./data/NA12878.bam
  ./data/NA12877.bam
  ./data/NA12879.bam

Genomic position
----------------

Single position (``-pos``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can add one or more genomic position(or region) with ``-pos`` option. 

.. code:: console

    $ bamsnap -bam ./data/NA12878.bam -pos chr1:7364529
    $ bamsnap -bam ./data/NA12878.bam -pos chr1:7364529 chr3:7364529 chr1:7364529
    $ bamsnap -bam ./data/NA12878.bam -pos chr1:7364509-7364559

If bam file doesn't use 'chr' string in chromosome (ex. 1:7364529), you should not use 'chr' string in the ``-pos`` option. 

VCF file (``-vcf``)
^^^^^^^^^^^^^^^^^^^

Bamsnap can read ``.vcf`` (raw file) and ``.vcf.gz`` (gzip or bgzip compressed vcf file).

.. code:: console

    $ bamsnap \
      -bam ./data/NA12878.bam \
      -vcf ./data/multiple_variants.vcf.gz \
      -out ./out/mutiple_variants_NA12878


BED file (``-bed``)
^^^^^^^^^^^^^^^^^^^

.. code:: console

    $ bamsnap \
      -bam ./data/NA12878.bam \
      -bed ./data/multiple_regions.bed \
      -out ./out/mutiple_regions_NA12878


Reference sequence file
-----------------------

Users should define sequence reference version or sequence reference fasta file. If users don't define reference fasta file (``-ref``), **BamSnap** can get the corresponding sequence from UCSC genome browser database (hg38). Currently, the default version of reference(``-refversion``) is ``hg38``. If you want to use hg19 version, you can use ``-refversion hg19``.


.. note:: 
  If you don't define ``-ref``, **BamSnap** can access UCSC genome browser database and get the corresponding sequence in every genomic positions. If you want to use **BamSnap** with multiple variants (positions or regions), we recommend that use ``-ref`` with a reference fasta file in local path. 


FASTA file (``-ref``)
^^^^^^^^^^^^^^^^^^^^^
.. code:: console

    $ bamsnap \
      -bam ./data/NA12879.bam_chr10_117542947.bam \
      -ref ./fasta/GRCh38_full_analysis_set_plus_decoy_hla.fa


.. note:: 
  When you add fasta file, **BamSnap** checks its index file (.fai). If the index file is not exist, **BamSnap** generates the index file automatically (this step would take a few minutes). 
  If the index file is older than the fasta file and you want to rebuild this index file, you can use ``-ref_index_rebuild`` option.
