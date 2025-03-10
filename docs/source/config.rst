.. _yaml: 

DLIO Configuration
==============================================
The characteristics of a workload is specified through a YAML file. This will then be read by the DLIO program to setup the benchmark. Below is an example of such a YAML file. More examples can be found in the `workload`_ folder. 

.. code-block:: yaml
  
  model: unet3d

  framework: pytorch

  workflow:
    generate_data: True
    train: True
    evaluation: True

  dataset: 
    data_folder: ./data/unet3d/
    format: npz
    num_files_train: 3620
    num_files_eval: 42
    num_samples_per_file: 1
    batch_size: 4
    batch_size_eval: 1
    file_access: multi
    record_length: 1145359
    keep_files: True
  
  data_reader: 
    data_loader: pytorch
    read_threads: 4
    prefetch: True

  train:
    epochs: 10
    computation_time: 4.59

  evaluation: 
    eval_time: 11.572
    epochs_between_evals: 2

A DLIO YAML configuration file contains following sections: 

* **model** - specifying the name of the model.
* **framework** - specifying the framework to use for the benchmark, options: tensorflow, pytorch
* **workflow** - specifying what workflow operations to perform, including dataset generation, training, evaluation, checkpointing, evaluation, debugging, etc. 
* **dataset** - specifying all the information related to the dataset. 
* **data_reader** - specifying the data loading options 
* **train** - specifying the setup for training
* **evaluation** - specifying the setup for evaluation. 
* **checkpoint** - specifying the setup for checkpointing. 
* **profiling** - specifying the setup for profiling

model
------------------
No other parameters under this section. 
One can specify the name of the model as 

.. code-block:: yaml

  model: unet3d

framework
-------------------
No parameters under this group. 
Specify the frameork (tensorflow or pytorch) as 

.. code-block:: yaml

  framework: tensorflow

workflow
------------------
.. list-table:: 
   :widths: 15 10 30
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - generate_data
     - False
     - whether to generate dataset
   * - train
     - True
     - whether to perform training
   * - evaluation
     - False
     - whether to perform evaluation
   * - checkpoint
     - False
     - whether to perform checkpointing
   * - profiling
     - False
     - whether to perform profiling

.. note:: 

  If ``train`` is set to be ```False```, ``evaluation``, ``checkpoint``, ``profiling`` will be set to ```False``` automatically. 

  Even though ``generate_data`` and ``train`` can be performed together in one job, we suggest to perform them seperately. One can generate the data first by running DLIO with ```generate_data=True``` and ```train=False```, and then run training benchmark with ```generate_data=False``` and ```train=True```. 

dataset
------------------
.. list-table:: 
   :widths: 15 10 30
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - record_length
     - 65536
     - size of each sample
   * - format
     - tfrecord
     - data format [tfrecord|csv|npz|jpeg|png]
   * - num_files_train
     - 1
     - number of files for the training set
   * - num_files_eval
     - 0
     - number of files for evaluation/validation set
   * - num_samples_per_file
     - 1
     - number of samples per file
   * - data_folder
     - ./data
     - the path to store the dataset
   * - num_subfolders_train
     - 0
     - number of subfolders that the training set is stored
   * - num_subfolders_eval
     - 0
     - number of subfolders that the evaluation/validation set is stored
   * - batch_size
     - 1 
     - batch size for training
   * - batch_size_eval
     - 1 
     - batch size for evaluation
   * - file_prefix
     - img
     - the prefix of the dataset file(s)
   * - compression
     - none
     - what compressor to use to compress the dataset. (limited support)
   * - compression_level
     - 4
     - level of compression for gzip
   * - chunking
     - False
     - whether to use chunking to store hdf5. 
   * - chunk_size
     - 0
     - the chunk size for hdf5. 
   * - keep_files
     - True
     - whether to keep the dataset files afer the simulation.    

data_reader 
------------------
.. list-table:: 
   :widths: 15 10 30
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - data_loader*
     - tensorflow
     - select the data loader to use [tensorflow|pytorch|node]. 
   * - read_threads
     - 1
     - number of threads to load the data (for tensorflow and pytorch data loader)
   * - computation_threads
     - 1
     - number of threads to preprocess the data
   * - prefetch
     - False
     - whether to prefetch the dataset
   * - prefetch_size
     - 0
     - number of batch to prefetch
   * - read_shuffle
     - off
     - [seed|random|off] whether and how to shuffle the dataset
   * - file_access
     - multi
     - multi - file per process; shared - independent access to a single shared file; collective - collective I/O access to a single shared file
   * - transfer_size
     - 1048576
     - transfer size in byte for tensorflow data loader. 

.. note:: 

  If ``none`` is set for ``data_reader.data_loader``, then custom 
  data reader such as ``npz_reader``, ``csv_reader``, ``hdf5_reader`` will be used. 
  Currently, these custom readers do not support advance features
  such as multiple read_threads, prefetch, etc. 

train
------------------
.. list-table:: 
   :widths: 15 10 30
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - epochs
     - 1
     - number of epochs to simulate
   * - computation_time
     - 0.0
     - emulated computation time per step in second
   * - total_training_steps
     - -1
     - number of training steps to simulate, assuming running the benchmark less than one epoch. 
   * - seed_change_epoch
     - True
     - whether to change random seed after each epoch
   * - seed
     - 123
     - the random seed     

evaluation
------------------
.. list-table:: 
   :widths: 15 10 30
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - eval_time
     - 0
     - emulated computation time (sleep) for each evaluation step. 
   * - epochs_between_evals
     - 0
     - evaluate after x number of epochs

checkpoint
------------------
.. list-table:: 
   :widths: 15 10 30
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - checkpoing_after_epoch
     - 0
     - start checkpointing after certain number of epochs specified 
   * - epochs_between_checkpoints
     - 0
     - performing one checkpointing per certain number of epochs specified
   * - steps_between_checkpoints
     - 0
     - performing one checkpointing per certain number of steps specified
   * - model_size
     - 10240
     - the size of the model in bytes

profiling
------------------
.. list-table:: 
   :widths: 15 10 30
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - profiler
     - none
     - specifying the profiler to use [none|iostat|tensorflow|pytorch]
   * - darshan_preload*
     - /usr/local/darshan-3.2.1/lib/libdarshan.so
     - specifying the DARSHAN LD_PRELOAD library.     
   * - iostat_command**
     - "iostat -mdxtcy -o JSON sda sdb 1"
     - specifying the command which will be used for iostat profiling.  

We support following I/O profiling using following profilers: 

  * ``darshan``: https://www.mcs.anl.gov/research/projects/darshan/. ``darshan_preload`` has to be set for the runtime library to be loaded properly. 

  * ``iostat``: https://linux.die.net/man/1/iostat. One can specify the command to use for profiling in order to get the profiling for specific disk.   
  * ``tensorflow`` (tf.profiler): https://www.tensorflow.org/api_docs/python/tf/profiler. This works only for tensorflow framework (and data loader)

  * ``pytorch`` (torch.profiler): https://pytorch.org/docs/stable/profiler.html. This works only for pytorch framework (and data loader).

The YAML files are stored in the `workload`_ folder. 
It then can be loaded by ```dlio_benchmark.py``` through hydra (https://hydra.cc/). This will override the default settings. One can override the configurations through command line (https://hydra.cc/docs/advanced/override_grammar/basic/). 


.. _workload: https://github.com/argonne-lcf/dlio_benchmark/tree/main/configs/workload