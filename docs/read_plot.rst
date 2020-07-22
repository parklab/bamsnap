Read alignment track (``-bamplot read``)
========================================


Layout options
--------------

.. image:: ./img/pic_read1.png
   :width: 70 %

* ``-read_thickness`` (default=5) : read thickness (unit:px)
* ``-read_gap_height`` (default=2) : read gap height (unit:px)
* ``-read_gap_width`` (default=2) : min size of read gap width (unit:px)
* ``-read_bgcolor`` (default='FFFFFF') : read background color
* ``-read_color`` (default='C8C8C8') : read color
* ``-center_line`` (default=false): draw center line
* ``-no_target_line`` (default=false): do not draw target line


.. code:: console

  $ bamsnap \
    -bam ./data/NA12879.bam \
    -pos chr10:117542948 \
    -no_title \
    -draw bamplot \
    -bamplot read \
    -out ./out/NATRIO_chr10_117542948_3.png \
    -read_thickness 15 \
    -read_gap_height 10 \
    -read_gap_width 5


Read group (``-read_group``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**BamSnap** supports to group by read strand with ``-read_group strand``. In this case, ``-read_pos_color`` and ``-read_neg_color`` can be used for changing the grouped read color.

* ``-read_pos_color`` (default='FFAC9C') : positive strand read color
* ``-read_neg_color`` (default='A19CFF') : negative strand read color

.. code:: console

  $ bamsnap \
    -bam ./data/NA12879.bam \
    -pos chr10:117542948 \
    -no_title \
    -draw bamplot \
    -bamplot read \
    -out ./out/NATRIO_chr10_117542948_6.png \
    -read_group strand

.. image:: ../tests/out/NATRIO_chr10_117542948_6.png
   :width: 100 %


