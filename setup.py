#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'pyfaidx>=0.5.3.1',
    'pysam>=0.11.2.2',
    'Pillow>=2.0.0',
    'pytabix>=0.0.2'
]

tests_require = [
    'nose',
    'mock'
]

extras_require = {
    'docs': [
        'Sphinx>=1.1'
    ]
}

setup(name='bamsnap',
      version='0.2.19',
      url='https://github.com/danielmsk/bamsnap',
      license='MIT',
      author='Daniel Minseok Kwon',
      author_email='daniel.minseok.kwon@gmail.com',
      description='A converter from .bam to .png for specific genomic region.',
      download_url='https://github.com/danielmsk/bamsnap/archive/0.1.tar.gz',
      keywords=['genomics', 'bioinformatics'],
      classifiers=[
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      # packages=find_packages(exclude=['tests']),
      packages=find_packages('src'),
      package_dir={'': 'src'},
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      zip_safe=False,
      install_requires=install_requires,
      setup_requires=['nose>=1.0'],
      test_suite='nose.collector',
      # packages = ['.','templates'],
      package_data={
          'bamsnap': ['templates/*', 'data/*'],
      },
      entry_points={
          'console_scripts': [
              'bamsnap=bamsnap:cli',
          ]
      })
