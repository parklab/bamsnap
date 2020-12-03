Installation
============

Prerequisites
-------------

* python 3.4+
* `Pillow (Python Imaging Library) (2.0.0+) <https://pypi.org/project/Pillow/>`_
* `pysam (0.11.2.2+) <https://pypi.org/project/pysam/>`_
* `pyfaidx (0.5.3.1+) <https://pypi.org/project/pyfaidx/>`_
* `pytabix (0.0.2+) <https://pypi.org/project/pytabix/>`_


Install with pypi
-----------------

To install **BamSnap** with pip run:

.. code:: console

  $ pip install bamsnap
  $ bamsnap


Install from source
-------------------

.. code:: console

  $ git clone https://github.com/parklab/bamsnap
  $ cd bamsnap
  $ python setup.py install
  $ bamsnap

Install from docker hub
-----------------------

.. code:: console

  $ docker pull danielmsk/bamsnap
  $ docker images

  REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
  danielmsk/bamsnap   latest              f9f6e61c7673        2 hours ago         997MB

  $ docker run --rm -it -v /local_directory_path:/directory_path_in_image \
    danielmsk/bamsnap bamsnap \
      -bam /directory_path_in_image/test.bam \
      -pos 1:7364529 \
      -out /directory_path_in_image/test.png

The docker image can be pulled from the docker hub site (https://hub.docker.com/r/danielmsk/bamsnap). When you are using bamsnap from docker image, you should assign the local directory path (volume) and the image direcotry path (volume) using ``-v`` option.