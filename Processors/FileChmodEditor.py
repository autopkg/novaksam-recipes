#!/usr/bin/env python
#
# Copyright 2015 Sam Novak
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import errno
import os

from autopkglib import Processor, ProcessorError


# this is from here:
# http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
def makedir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


class FileChmodEditor(Processor):
    description = """Modifies the access for files using chmod."""

    input_variables = {
        "pathname": {
            "required": True,
            "description": "Path to where the file you want to modify is"
        },
        "modifier": {
            "required": True,
            "description": """Modifier to change to (in 444 format)"""
        }
    }

    output_variables = {
    }

    __doc__ = description



    def main(self):

        os.chmod(self.env["pathname"],int(self.env["modifier"],8))



if __name__ == '__main__':
    processor = FileChmodEditor()
    processor.execute_shell()
