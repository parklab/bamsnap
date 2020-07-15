Input files
===========
BamSnap supports 


Alignment file
--------------

BAM file (-bam)
^^^^^^^^^^^^^^^


Genomic position
----------------

Single position (-pos)
^^^^^^^^^^^^^^^^^^^^^^


VCF file (-vcf)
^^^^^^^^^^^^^^^
Bamsnap can read `.vcf(raw file)` and `.vcf.gz(gzip or bgzip compressed vcf file)`. 


BED file (-bed)
^^^^^^^^^^^^^^^

Reference sequence file
-----------------------

Users should define sequence reference version or sequence reference fasta file. If users don't define reference fasta file (``-ref``), bamsnap can get the corresponding sequence from UCSC genome browser database. Currently, the default version of reference(``-refversion``) is ``hg38``. 


.. note:: 
    If the user does not define ``-ref``, 


FASTA file (-ref)
^^^^^^^^^^^^^^^^^
.. code:: console

    $ bamsnap \
      -bam ./data/NA12879.bam_chr10_117542947.bam \
      -ref 
