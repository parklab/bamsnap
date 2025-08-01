# BamSnap

BamSnap: a lightweight command-based visualization tool for sequencing reads in BAM files

<!--<img src="https://raw.githubusercontent.com/parklab/bamsnap/master/data/ex1/snapfiles/snap_test11.bam_1_715347-715348.png" height=128px width=405px>-->

For more details, see BamSnap [**Documentation**](http://bamsnap.readthedocs.io/en/latest).

[<img src="https://img.shields.io/pypi/v/bamsnap.svg">](https://pypi.org/project/bamsnap/)
[<img src="https://img.shields.io/pypi/dm/bamsnap.svg">](https://pypi.org/project/bamsnap/)
[<img src="https://readthedocs.org/projects/bamsnap/badge/?version=latest">](https://bamsnap.readthedocs.io/)
[<img src="https://img.shields.io/docker/pulls/danielmsk/bamsnap.svg">](https://hub.docker.com/r/danielmsk/bamsnap)

## Installation

### Prerequisites (installed via pip)

BamSnap (>= v1.0.0) requires Python 3.9+. It uses Pillow, pysam, pyfaidx and pytabix under the hood.

### Install with pip (NOT WORKING FOR V1 YET!)

```bash
pip install bamsnap 
```
* [pypi site for bamsnap](https://pypi.org/project/bamsnap/)

### Install from source

```
git clone https://github.com/parklab/bamsnap
cd bamsnap
make build
```

## Usage

### Simple usage examples
```bash
$ bamsnap --bam test.bam --pos chr1:7364529 --out test.png
$ bamsnap --bam test1.bam --bam test2.bam --title "BAM Test 1" --title "BAM Test 2" --pos chr1:7364529 --out test.png
```

For more details, see BamSnap [**Documentation**](http://bamsnap.readthedocs.io/en/latest).

### Usage with docker
```bash
$ docker pull aveit/bamsnap
$ docker run --rm -it -v /local_directory_path:/directory_path_in_image aveit/bamsnap bamsnap \
    --bam /directory_path_in_image/test.bam \
    --pos chr1:7364529 \
    --out /directory_path_in_image/test.png
```


## Example Use Case

* [**1000 Genome Data**](https://bamsnap-1kg.s3.amazonaws.com/index.html): 1000 genomic loci in 2504 individuals
* [**BamSnap Plot Gallery**](https://bamsnap.readthedocs.io/en/latest/gallery.html)





