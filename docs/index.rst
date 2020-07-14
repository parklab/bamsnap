.. BamSnap documentation master file, created by
   sphinx-quickstart on Thu Jan  9 14:40:53 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

BamSnap
=======

BamSnap is a high-performance visualization tool for aligned BAM file based on command-line interface.

.. image:: https://raw.githubusercontent.com/parklab/bamsnap/master/tests/out/NATRIO_chr10_117542948.png
   :width: 100 %

Quick run
---------
.. code:: console

  $ pip install bamsnap
  $ bamsnap -bam test.bam -pos chr1:7364529 -out test.bam.png


You can find more BamSnap examples and commands in `gallary <gallary.html>`_.


Contents
--------

.. toctree::
   :maxdepth: 4

   installation
   gallary
   options
   input
   output
   coverage_plot
   read_plot
   base_plot
   gene_plot
   read_group
   version_history

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
