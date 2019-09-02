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

from __future__ import absolute_import, print_function

import os.path
import traceback

import xattr
from autopkglib import Processor, ProcessorError
from autopkglib.DmgMounter import DmgMounter


class ResourceForkCopier(DmgMounter):
    description = """Copies Resource Forks (because copier can't)"""

    input_variables = {
        "source_file": {
            "required": True,
            "description": "Path to the file with the Resource Fork you want to copy."
        },
        "destination_file": {
            "required": True,
            "description": """File you want the Resource Fork copied to."""
        }
    }

    output_variables = {
    }

    __doc__ = description

    def main(self):

        source_file = self.env['source_file']
        destination_file = self.env["destination_file"]
        # Check if we're trying to copy something inside a dmg.
        (dmg_path, dmg, dmg_source_path) = self.parsePathForDMG(source_file)
        try:
            if dmg:
                # Mount dmg and copy path inside.
                mount_point = self.mount(dmg_path)
                source_file = os.path.join(mount_point, dmg_source_path)
                source_file = source_file.decode("string_escape")
                destination_file = destination_file.decode("string_escape")
                xattr.listxattr(source_file)
                temp = xattr.getxattr(source_file, "com.apple.ResourceFork")
                xattr.setxattr(destination_file, "com.apple.ResourceFork", temp)
                self.output("Resource Fork copied")
        except:
            var = traceback.format_exc()
            print(("ERROR:", var))
            self.output("Resoruce Fork error: " + var)
        finally:
            if dmg:
                self.unmount(dmg_path)


if __name__ == '__main__':
    processor = ResourceForkCopier()
    processor.execute_shell()
