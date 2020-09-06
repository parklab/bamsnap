# <img src="https://bampdx.com/wp-content/uploads/2015/12/BAMPDX-logo.png" height=28px width=45px>&nbsp;BAMsnap
<!--[![Build Status](https://travis-ci.org/bamsnap/bamsnap.svg?branch=develop)](https://travis-ci.org/bamsnap/bamsnap) 
[![Code Health](https://landscape.io/github/bamsnap/bamsnap/develop/landscape.svg?style=flat)](https://landscape.io/github/bamsnap/bamsnap/develop) 
[![Coverage Status](https://img.shields.io/codecov/c/github/bamsnap/bamsnap/develop.svg)](https://codecov.io/github/bamsnap/bamsnap?branch=develop)-->

BAMSNAP is high-performed command-based visualization tool for the aligned BAM file.

<!--<img src="https://raw.githubusercontent.com/parklab/bamsnap/master/data/ex1/snapfiles/snap_test11.bam_1_715347-715348.png" height=128px width=405px>-->

For more details, see BamSnap [**Documentation**](http://bamsnap.readthedocs.io/en/latest).

[<img src="https://img.shields.io/pypi/v/bamsnap.svg">](https://pypi.org/project/bamsnap/)
[<img src="https://img.shields.io/pypi/dm/bamsnap.svg">](https://pypi.org/project/bamsnap/)
[<img src="https://readthedocs.org/projects/bamsnap/badge/?version=latest">](https://bamsnap.readthedocs.io/)

## Installation

### Prerequisites
* python 3.4+
* [Pillow (Python Imaging Library)](https://pypi.org/project/Pillow/)
* [pysam](https://pypi.org/project/pysam/)
* [pyfaidx](https://pypi.org/project/pyfaidx/)
* [pytabix](https://pypi.org/project/pytabix/)

### Install with pip

```bash
pip install bamsnap
```
* [pypi site for bamsnap](https://pypi.org/project/bamsnap/)

### Install with github

```
git clone https://github.com/parklab/bamsnap
cd bamsnap
python setup.py install
```

## Usage

### Simple usage
```bash
$ bamsnap -bam test.bam -pos 1:7364529 -out test.png
```

For more details, see BamSnap [**Documentation**](http://bamsnap.readthedocs.io/en/latest).


## Examples Use Case

* [**1000 Genome Data**](http://100.26.138.46:8000/)
* [**BamSnap Plot Gallery**](https://bamsnap.readthedocs.io/en/latest/gallery.html)





