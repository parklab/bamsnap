#!/usr/bin/env python3
"""
BAMSNAP - A lightweight tool for making snapshots of BAM files
Click-based CLI interface
"""

import click
import sys
import os
from typing import List, Tuple, Optional
from .bamsnap import BamSnap

# Add the bamsnap module to the path
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'bamsnap'))


@click.command()
# Input files
@click.option('--bam', multiple=True, help='bam or cram file(s)')
@click.option('--bamlist', type=click.Path(exists=True), help='list file with bam (or cram) file paths')
@click.option('--title', multiple=True, help='title (name) of bam (or cram) file(s)')
@click.option('--no-title', is_flag=True, help='do not draw label.')
@click.option('--title-fontsize', type=int, default=18, help='font size of title')

# Genomic positions
@click.option('--pos', multiple=True, help='genomic position (ex. 1:816687-818057, chr12:7462545)')
@click.option('--vcf', type=click.Path(exists=True), help='list file with genomic positions with VCF format')
@click.option('--bed', type=click.Path(exists=True), help='list file with genomic positions with BED format')

# Output options
@click.option('--out', default='bamsnap_out', help='output file or directory name for all output files')
@click.option('--imagetype', type=click.Choice(['png', 'jpg']), default='png', help='output file type')
@click.option('--conf', help='configuration file')
@click.option('--save-image-only', is_flag=True, help='save image only')
@click.option('--image-dir-name', default='bamsnap_images', help='image directory name')
@click.option('--zipout', is_flag=True, help='make a single zip file')

# Reference options
@click.option('--ref', help='Reference sequence fasta file (ex. hg19.fa)')
@click.option('--ref-index-rebuild', is_flag=True, help='if you want to rebuild fasta index file (.fai), when it is older than the fasta file. (Default: false)')
@click.option('--refversion', type=click.Choice(['hg19', 'hg38']), default='hg38', help='Reference version (default: hg38)')

# Layout options
@click.option('--margin', type=int, default=50, help='genomic margin size')
@click.option('--separator-height', type=int, default=30, help="separator's height")
@click.option('--process', type=int, default=1, help='number of process for multi-processing (default: 1)')

# Track composition
@click.option('--draw', default="coordinates,bamplot,base,gene", 
              help='track composition (default: coordinates,bamplot,base,gene)')
@click.option('--bamplot', default="coverage,base,read",
              help='track composition of bamplot (default: coverage,base,read)')

# Image dimensions and appearance
@click.option('--width', type=int, default=1000, help='image width (unit:px, default: 1000)')
#@click.option('--height', type=int, help='image height (unit:px)')
@click.option('--bgcolor', default='FFFFFF', help='background color (default: FFFFFF)')
@click.option('--plot-margin-top', type=int, default=20, help='top margin size of plot (default: 20)')
@click.option('--plot-margin-bottom', type=int, default=20, help='bottom margin size of plot (default: 20)')
@click.option('--plot-margin-left', type=int, default=0, help='left margin size of plot (default: 0)')
@click.option('--plot-margin-right', type=int, default=0, help='right margin size of plot (default: 0)')
@click.option('--border', is_flag=True, help='draw border in plot (default: false)')
@click.option('--grid', type=int, default=0, help='draw grid in plot (default: 0 (grid size))')

# Read appearance
@click.option('--read-thickness', type=int, default=5, help='read thickness (unit:px)')
@click.option('--read-gap-height', type=int, default=2, help='read gap height (unit:px)')
@click.option('--read-gap-width', type=int, default=2, help='min size of read gap width (unit:px)')
@click.option('--read-bgcolor', default='FFFFFF', help='read background color')
@click.option('--read-color', default='C8C8C8', help='read color')
@click.option('--read-pos-color', default='FFAC9C', help='positive strand read color')
@click.option('--read-neg-color', default='A19CFF', help='negative strand read color')
@click.option('--read-color-deletion', default='FF0000', help='read color of deletion')
@click.option('--read-color-inversion', default='485BA9', help='read color of inversion')

# Insert size thresholds
@click.option('--insert-size-del-threshold', type=int, default=1000, help='insert size threshold for deletion (default: 1000)')
@click.option('--insert-size-ins-threshold', type=int, default=50, help='insert size threshold for insertion (default: 50)')

# Read grouping and coloring
@click.option('--read-group', type=click.Choice(['strand']), help='read group')
@click.option('--read-color-by', type=click.Choice(['strand', 'interchrom']), help='read color by')

# Chromosome-specific colors for interchromosomal reads
@click.option('--read-color-interchrom-chr1', default='64689b', help='paired read color located in chromosome 1')
@click.option('--read-color-interchrom-chr2', default='D6503A', help='paired read color located in chromosome 2')
@click.option('--read-color-interchrom-chr3', default='87AA62', help='paired read color located in chromosome 3')
@click.option('--read-color-interchrom-chr4', default='F2EB89', help='paired read color located in chromosome 4')
@click.option('--read-color-interchrom-chr5', default='597E98', help='paired read color located in chromosome 5')
@click.option('--read-color-interchrom-chr6', default='C5763E', help='paired read color located in chromosome 6')
@click.option('--read-color-interchrom-chr7', default='70BFE7', help='paired read color located in chromosome 7')
@click.option('--read-color-interchrom-chr8', default='91307F', help='paired read color located in chromosome 8')
@click.option('--read-color-interchrom-chr9', default='80DE6E', help='paired read color located in chromosome 9')
@click.option('--read-color-interchrom-chr10', default='DCA5B5', help='paired read color located in chromosome 10')
@click.option('--read-color-interchrom-chr11', default='A35A24', help='paired read color located in chromosome 11')
@click.option('--read-color-interchrom-chr12', default='978DA0', help='paired read color located in chromosome 12')
@click.option('--read-color-interchrom-chr13', default='D16525', help='paired read color located in chromosome 13')
@click.option('--read-color-interchrom-chr14', default='DCA167', help='paired read color located in chromosome 14')
@click.option('--read-color-interchrom-chr15', default='8C79B9', help='paired read color located in chromosome 15')
@click.option('--read-color-interchrom-chr16', default='E9BD71', help='paired read color located in chromosome 16')
@click.option('--read-color-interchrom-chr17', default='4B2669', help='paired read color located in chromosome 17')
@click.option('--read-color-interchrom-chr18', default='D7E4BF', help='paired read color located in chromosome 18')
@click.option('--read-color-interchrom-chr19', default='733B91', help='paired read color located in chromosome 19')
@click.option('--read-color-interchrom-chr20', default='BC2D7A', help='paired read color located in chromosome 20')
@click.option('--read-color-interchrom-chr21', default='EBD176', help='paired read color located in chromosome 21')
@click.option('--read-color-interchrom-chr22', default='6E786F', help='paired read color located in chromosome 22')
@click.option('--read-color-interchrom-chrx', default='D5AA00', help='paired read color located in chromosome X')
@click.option('--read-color-interchrom-chry', default='A9D400', help='paired read color located in chromosome Y')
@click.option('--read-color-interchrom-other', default='555555', help='paired read color located in other chromosome')

# Clipping options
@click.option('--show-soft-clipped', is_flag=True, help='show soft clipped part (default: false)')
@click.option('--show-hard-clipped', is_flag=True, help='show hard clipped part (default: false)')
@click.option('--show-clipped', is_flag=True, help='show soft and hard clipped part (default: false)')

# Line options
@click.option('--center-line', is_flag=True, help='draw center line')
@click.option('--no-target-line', is_flag=True, help='do not draw target line')

# Base track options
@click.option('--base-fontsize', type=int, default=9, help='font size of base track')
@click.option('--base-height', type=int, default=30, help='base track height')
@click.option('--base-margin-top', type=int, default=0, help='top margin size of base track')
@click.option('--base-margin-bottom', type=int, default=0, help='bottom margin size of base track')

# Coverage track options
@click.option('--coverage-height', type=int, default=40, help='coverage track height')
@click.option('--coverage-fontsize', type=int, default=9, help='coverage font size')
@click.option('--coverage-vaf', type=float, default=0.2, help='coverage variant allele fraction threshold (default: 0.2)')
@click.option('--coverage-color', default='A3A3A3', help='coverage color')
@click.option('--coverage-bgcolor', default='FFFFFF', help='coverage track background color')

# Heatmap options
@click.option('--heatmap-height', type=int, default=5, help='coverage heatmap height')
@click.option('--heatmap-bgcolor', default='FFFFFF', help='coverage heatmap background color')

# Gene track options
@click.option('--gene-height', type=int, default=50, help='gene track height')
@click.option('--gene-fontsize', type=int, default=10, help='font size of gene track')
@click.option('--gene-pos-color', default='FFAC9C', help='positive strand color')
@click.option('--gene-neg-color', default='A19CFF', help='negative strand color')

# Coordinates track options
@click.option('--coordinates-height', type=int, default=20, help='coordinate height')
@click.option('--coordinates-fontsize', type=int, default=12, help='coordinate font size')
@click.option('--coordinates-axisloc', type=click.Choice(['top', 'bottom', 'middle']), default='bottom', help='coordinate axis location')
@click.option('--coordinates-bgcolor', default='FFFFFF', help='coordinate background color')
@click.option('--coordinates-labelcolor', default='000000', help='coordinate label color')

# Other options
@click.option('--separated-bam', is_flag=True, help='draw a plot for each bam')
@click.option('--debug', is_flag=True, help='turn on the debugging mode')
@click.option('--silent', is_flag=True, help='Do not print any messages to stdout')
def main(**kwargs):
    """
    BAMSNAP - A lightweight tool for making snapshots of BAM files
    """
    bs = BamSnap(kwargs)
    bs.run()


# def convert_click_args_to_namespace(kwargs):
#     """Convert click arguments to argparse-like namespace object"""
#     import argparse
    
#     # Convert click argument names back to underscore format expected by the original code
#     converted = {}
#     for key, value in kwargs.items():
#         # Convert kebab-case back to underscore format
#         converted_key = key.replace('-', '_')
#         converted[converted_key] = value
    
#     # Convert certain arguments to lists if they were passed as tuples
#     list_args = ['bam', 'title', 'pos', 'draw', 'bamplot']
#     for arg in list_args:
#         if arg in converted and isinstance(converted[arg], tuple):
#             converted[arg] = list(converted[arg])
    
#     # Create namespace object
#     return argparse.Namespace(**converted)


if __name__ == "__main__":
    main()
