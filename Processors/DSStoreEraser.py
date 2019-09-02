#!/usr/bin/env python
#
# Copyright 2015 Sam Novak
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import re

from autopkglib import Processor, ProcessorError


class DSStoreEraser(Processor):
    description = """Given a text file, will read and the and exclude lines containing DS_Store"""

    input_variables = {
        "file_path": {
            "required": True,
            "description": "Path to where the file you want to modify is"
        }
    }

    output_variables = {
    }

    __doc__ = description



    def main(self):
        inputfile = open(self.env["file_path"], 'r')
        temp = (re.sub(r"(.*?)DS_Store", "", inputfile.read()))
        outputfile = open(self.env["file_path"], 'w')
        outputfile.write(temp)
        inputfile.close()
        outputfile.close()


if __name__ == '__main__':
    processor = DSStoreEraser()
    processor.execute_shell()
