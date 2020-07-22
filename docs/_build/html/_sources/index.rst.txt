.. BamSnap documentation master file, created by
   sphinx-quickstart on Thu Jan  9 14:40:53 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

BamSnap
=======

.. image:: https://img.shields.io/pypi/v/bamsnap.svg
   :target: https://pypi.org/project/bamsnap/
   :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/bamsnap.svg
   :target: https://pypi.org/project/bamsnap/
   :alt: Number of PyPI downloads

.. image:: https://readthedocs.org/projects/bamsnap/badge/?version=latest
   :target: https://bamsnap.readthedocs.io/en/latest/
   :alt: Documentation of BamSnap

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


BamSnap is open-source and can be found on `github <https://github.com/parklab/bamsnap>`_.




Contents
--------

.. toctree::
   :numbered:
   :maxdepth: 4

   installation.rst
   gallary.rst
   options.rst
   input.rst
   output.rst
   plot.rst
   read_plot.rst
   coverage_plot.rst
   base_plot.rst
   gene_plot.rst
   coordinates_plot.rst
   heatmap.rst
   version_history.rst

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
