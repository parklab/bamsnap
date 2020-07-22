.. BamSnap documentation master file, created by
   sphinx-quickstart on Thu Jan  9 14:40:53 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

BamSnap
=======

**BamSnap** is a high-performance visualization tool for aligned BAM file. **BamSnap** is a command line program written in python. All commands involve typing ``bamsnap`` at the command prompt (e.g. DOS window or Unix termninal) followed by a number of options to specify the data files / parameters to be used. 

.. image:: ../tests/out/NATRIO_chr10_117542948.png
   :width: 100 %

Running BamSnap
---------------
**BamSnap** is a command-line program. Open up a command prompt or terminal window and take all bam snapshots by typing commands as described below. 


.. code:: console

  $ pip install bamsnap
  $ bamsnap -bam test.bam -pos chr1:7364529 -out test.bam.png


You can find more examples and commands in `gallary <gallary.html>`_. Use ``-h`` for options to be used with ``bamsnap``. 


.. code:: console

  $ bamsnap -h


Contents
--------

.. toctree::
   :maxdepth: 4

   installation
   gallary
   options
   input
   output
   plot
   read_plot
   coverage_plot
   base_plot
   gene_plot
   version_history

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
