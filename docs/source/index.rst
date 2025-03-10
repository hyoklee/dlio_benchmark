.. DLIO documentation master file

Deep Learning I/O Benchmark
===============================================================
Deep Learning I/O (DLIO) Benchmark is a benchmark suite aiming at emulating the I/O pattern / behavior of deep learning applications. The benchmark is delivered as an executable that can be configured for various deep learning specific I/O patterns. It uses a modular design to incorporate different data loaders, data formats, dataset organizations, and training configuration parameters to make it able to represent a broad spectrum of applications. The code is composed of four modules: **Benchmark Runner**, **Data Generator**, **Format Handler**, and **I/O Profiler**. 

The main features of DLIO include: 
   * Easy-to-use configuration through YAML config files to represent the I/O behavior of different deep learing applications.
   * Easy-to-use data generator to generate synthetic datasets of different formats, different data organizations and layouts. 
   * Full transparency over emulation of I/O access with logging and profiling at different levels with modern profilers such as Tensorboard, Torch profiler, darshan and iostat, etc. 
   * Supporting emulating both sequential and distributed data parallel training. 

GitHub repo: https://github.com/argonne-lcf/dlio_benchmark. 

.. toctree::
   :maxdepth: 2
   :caption: Overview

   overview

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   install
   config
   run
   examples

.. toctree::
   :maxdepth: 2
   :caption: Tested systems and Known issues

   knownissues
   
.. toctree::
   :maxdepth: 2
   :caption: How to contribute

   contribute

.. toctree::
   :maxdepth: 2
   :caption: Resources

   resources

.. toctree::
   :maxdepth: 2
   :caption: Legal

   copyright
   license
   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
