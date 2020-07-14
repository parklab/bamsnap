Base plot (-draw base, -bamplot base)
=====================================


Base plot has three types. 

.. image:: https://raw.githubusercontent.com/parklab/bamsnap/master/tests/out/NATRIO_chr10_117542948_baseplot_ex1.png
   :width: 100 %

.. code:: console

  $ bamsnap 
    -bam ./data/NA12879.bam_chr10_117542947.bam \
    -title "NA12879 (Daughter)" \
    -draw bamplot \
    -bamplot coverage base \
    -pos chr10:117542948 \
    -separator_height 0 \
    -margin 500 \
    -no_title \
    -width 700 \
    -plot_margin_top 0 \
    -plot_margin_bottom 0 \
    -out ./out/NATRIO_chr10_117542948_baseplot_ex1.png


.. image:: https://raw.githubusercontent.com/parklab/bamsnap/master/tests/out/NATRIO_chr10_117542948_baseplot_ex2.png
   :width: 100 %

.. code:: console

  $ bamsnap 
    -bam ./data/NA12879.bam_chr10_117542947.bam \
    -title "NA12879 (Daughter)" \
    -draw bamplot \
    -bamplot coverage base \
    -pos chr10:117542948 \
    -separator_height 0 \
    -margin 50 \
    -no_title \
    -width 700 \
    -plot_margin_top 0 \
    -plot_margin_bottom 0 \
    -out ./out/NATRIO_chr10_117542948_baseplot_ex2.png

.. image:: https://raw.githubusercontent.com/parklab/bamsnap/master/tests/out/NATRIO_chr10_117542948_baseplot_ex3.png
   :width: 100 %

.. code:: console

  $ bamsnap 
    -bam ./data/NA12879.bam_chr10_117542947.bam \
    -title "NA12879 (Daughter)" \
    -draw bamplot \
    -bamplot coverage base \
    -pos chr10:117542948 \
    -separator_height 0 \
    -margin 10 \
    -no_title \
    -width 700 \
    -plot_margin_top 0 \
    -plot_margin_bottom 0 \
    -out ./out/NATRIO_chr10_117542948_baseplot_ex3.png
