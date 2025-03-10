'''
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
'''   

from src.common.enumerations import ComputationType
from src.common.error_code import ErrorCodes
from src.computation.asynchronous_computation import AsyncComputation
from src.computation.no_computation import NoComputation
from src.computation.synchronous_computation import SyncComputation


class ComputationFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def get_handler(type):
        if type == ComputationType.NONE:
            return NoComputation()
        elif type == ComputationType.ASYNC:
            return AsyncComputation()
        elif type == ComputationType.SYNC:
            return SyncComputation()
        else:
            raise Exception(str(ErrorCodes.EC1000))
