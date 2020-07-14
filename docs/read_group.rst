Read group (-read_group)
=======================


Group by strand (-read_group strand)
------------------------------------

-read_group strand


.. image:: https://raw.githubusercontent.com/parklab/bamsnap/master/tests/out/NATRIO_chr10_117542948_1.png
   :width: 100 %


.. image:: https://raw.githubusercontent.com/parklab/bamsnap/master/tests/out/NATRIO_chr10_117542948.png
   :width: 100 %

.. code:: console

  $ bamsnap 
    -bam ./data/NA12879.bam_chr10_117542947.bam \
    -title "NA12879 (Daughter)" \
    -pos chr10:117542948 \
    -out ./out/NATRIO_chr10_117542948.png \
    -read_group strand


