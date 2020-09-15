Version History
===============

v0.2.x release series
---------------------
0.2.12 (2020.09.15):
	- adjust target line for deletion in VCF

0.2.11 (2020.09.08):
	- adjust target line

0.2.10 (2020.09.08):
	- debug ValueError when MD tag of read is missing (`issue #5<https://github.com/parklab/bamsnap/issues/5>`_)

0.2.9 (2020.09.03):
	- add ``insert_size_del_threshold`` for deletion, ``insert_size_ins_threshold`` for insertsion
	- add ``read_color_deletion`` for deletion, ``read_color_insersion`` for insertion

0.2.8 (2020.08.25):
	- add ``show_soft_clipped`` option to show soft clipped part of reads. (=> `manual <read_plot.html#read-color-read-color-by>`_ and `issue #4<https://github.com/parklab/bamsnap/issues/4>`_)

0.2.7 (2020.08.24):
	- add ``-read_color_by`` option for strand and inter-chromosomal rearrangement (=> `manual <read_plot.html#read-color-read-color-by>`_ )
	- convert pileup-based to fetch-based for read retrieval in `drawreadset.py <https://github.com/parklab/bamsnap/blob/master/src/bamsnap/drawreadset.py>`_

0.2.6 (2020.07.22):
	- debug in saving JPG file.
	- debug in coodinates axis location (middle)
	- debug in base font size.
	- update document.

0.2.5 (2020.07.17):
	- add multiprocessing option(``-process``)

0.2.4 (2020.07.15):
	- fix bug in version number
	- add separator height option
	- add -ref_index_rebuild option (to prevent to rebuild a fasta index file, when the fasta index file is older than the fasta file.)
	- update documentation

0.2.2 (2020.07.09):
	- debug typos

0.2.0 (2020.06.09):
	- add gene plot
	- add base plot
	- improve layout
	- add coordinates
	- add read group


v0.1.x release series
---------------------

0.1 :
	- basic read alignment view



Todo
----

- add SVG output
- add PDF output
- add bamviewer
