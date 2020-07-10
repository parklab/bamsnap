Gallary
=======

.. image:: https://raw.githubusercontent.com/parklab/bamsnap/master/tests/out/NATRIO_chr9:114786933.png
   :width: 100 %

.. code:: console

  $ bamsnap 
     -bam ./data/NA12877.bam_chr9_114786932.bam \
          ./data/NA12878.bam_chr9_114786932.bam \
          ./data/NA12879.bam_chr9_114786932.bam \
     -title "NA12877 (Father)" "NA12878 (Mother)" "NA12879 (Daughter)" \
     -pos chr9:114786933 \
     -out ./out/NATRIO_chr9:114786933.png \
     -draw coordinates bamplot base gene \
     -bamplot coverage base read \
     -margin 50 \
     -read_group strand \
     -plot_margin_left 20 \
     -plot_margin_right 20 \
     -border


