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

from src.profiler.io_profiler import IOProfiler
import tensorflow as tf
import os 

class TFProfiler(IOProfiler):
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if TFProfiler.__instance is None:
            TFProfiler()
        return TFProfiler.__instance

    def __init__(self):
        super().__init__()
        """ Virtually private constructor. """
        if TFProfiler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TFProfiler.__instance = self
        self.logdir = os.path.join(self.output_folder, "tf_logdir/")
    def start(self):
        tf.profiler.experimental.start(self.logdir)

    def stop(self):
        tf.profiler.experimental.stop()
