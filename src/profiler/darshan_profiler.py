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
import os

class DarshanProfiler(IOProfiler):
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DarshanProfiler.__instance is None:
            DarshanProfiler()
        return DarshanProfiler.__instance

    def __init__(self):
        super().__init__()
        self.darshan_preload = self._args.darshan_preload
        """ Virtually private constructor. """
        if DarshanProfiler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DarshanProfiler.__instance = self

    def start(self):
        #  this has to be changed to allow specifying DARSHAN librrary through DARSHAN_PRELOAD
        os.environ["LD_PRELOAD"] = args.darshan_preload
        os.environ["DXT_ENABLE_IO_TRACE"] = "1"
        os.environ["DARSHAN_DISABLE"] = "0"

    def stop(self):
        del os.environ['LD_PRELOAD']
        del os.environ['DXT_ENABLE_IO_TRACE']
