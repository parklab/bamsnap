Version History
===============


v0.3
----

0.3.19 (2020.05.25) :
	- split pred and score in pathogenicity score from VEP (SIFT and Polyphen)
	- add 'region_vcf' option in 'makedata'
0.3.18 (2020.05.13) :
	- add chain file option for pyliftover
0.3.17 (2020.05.06) :
	- add is_most_severe_transcript in external function.py
	- add keep_equal_str filter in data structure file
	- update -geno_info option to get sample ID list (ex. -geno_info HG002 HG003 HG004 )
	- update hgvs chromosome.
0.3.16 (2020.04.27) :
	- add GENE_MAIN_CHROM, CODING_GENE_MAIN_CHROM in -vartype option
0.3.15 (2020.03.26) :
	- add 'web' option
0.3.14 (2020.03.21) :
	- implement pypi installation
	- apply pytest
0.3.13 (2020.03.10) :
	- add 'add_genoinfo' option
	- add 'split_multi_allelic_variant' option
	- add 'clean_tag' option
0.3.12 (2020.03.05) :
	- add 'default' value
0.3.11 (2020.02.28) :
	- add SAMPLEGENO tag
	- minor fix in header
0.3.10 (2020.02.26) :
	- minor update in version tag
0.3.9 (2020.02.26) :
	- remove unannotated variant (-remove_unannotated_variant)
	- update the format of multiallele tag
0.3.8 (2020.02.25)
	- debugged first variant missing in annot module
0.3.7
	- update annot module
0.3.6
	- add makedata	
0.3.5
	- merge some dbNSFP fields into transcript table (dbNSFPTranscript)
0.3.4
	- change type of `dbNSFP SiPhy_29way_pi` to list
0.3.3
	- encode 'space' to '%20' (remove blank space)









