"""
   Copyright 2021 UChicago Argonne, LLC

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import math
import logging
from time import time

from src.utils.utility import utcnow
from src.common.enumerations import Shuffle, FormatType
from src.reader.reader_handler import FormatReader
import tensorflow as tf
import numpy as np

class TFDataLoaderReader(FormatReader):
    """
    Reader for TFRecord files.
    """
    def __init__(self, dataset_type):
        super().__init__(dataset_type)
        self.read_threads = self._args.read_threads
        self.computation_threads = self._args.computation_threads
        self.format = self._args.format
    # TODO: DLIO assumes the tfrecord files to contain image/label pairs.
    # This is not always the case, e.g. in BERT, each record is more complex,
    # consisting of 6 lists and a label. Same for DLRM. 
    @tf.function
    def _tf_parse_function(self, filename):
        """
        performs deserialization of the tfrecord.
        :param serialized: is the serialized version using protobuf
        :return: deserialized image and label.
        """
        if self.format==FormatType.NPZ:
            x = tf.io.read_file(filename)
            return x
        elif self.format==FormatType.JPEG:
            img = tf.io.read_file(filename)
            img = tf.image.decode_jpeg(img, channels=3)
            return img
        elif self.format==FormatType.PNG:
            img = tf.io.read_file(filename)
            img = tf.image.decode_png(img, channels=3)
            return img
        else:
            print("Reading %f format using Tensorflow Data Loader is not implemented, reading as bytes contents directly" %self.format)
            return tf.io.read_file(filename)

    def read(self, epoch_number):
        """
        Sets up the tf data pipeline to read tf record files.
        Called once at the start of every epoch.
        Does not necessarily read in all the data at the start however.
        :param epoch_number:
        """
        # superclass function initializes the file list
        super().read(epoch_number)
        dataset = tf.data.Dataset.from_tensor_slices(self._file_list)
        dataset = dataset.shard(num_shards=self.comm_size, index=self.my_rank)
        dataset = dataset.map(self._tf_parse_function, num_parallel_calls=self.read_threads)

        if self.memory_shuffle != Shuffle.OFF:
            if self.memory_shuffle != Shuffle.SEED:
                dataset = dataset.shuffle(buffer_size=self.shuffle_size,
                                          seed=self.seed)
            else:
                dataset = dataset.shuffle(buffer_size=self.shuffle_size)
        if self.prefetch:
            dataset = dataset.prefetch(buffer_size=self.prefetch_size)
        self._dataset = dataset.batch(self.batch_size, drop_remainder=True)


    def next(self):
        """
        Provides the iterator over tfrecord data pipeline.
        :return: data to be processed by the training step.
        """
        super().next()
        dataset = self._dataset

        # In tf, we can't get the length of the dataset easily so we calculate it
        if self._debug:
            total = math.ceil(self.num_samples*len(self._file_list)/self.batch_size/self.comm_size)
            logging.debug(f"{utcnow()} Rank {self.my_rank} should read {total} batches")

        # The previous version crashed when all workers could not generate the same amount of batches
        # Using the inbuilt tensorflow dataset iteration seems to work fine, was there an advantage of doing it the old way?
        # t1
        for batch in dataset:
            yield batch

    def finalize(self):
        pass
