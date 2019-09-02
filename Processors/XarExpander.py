#!/usr/bin/python
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

import os.path
import subprocess

from autopkglib import Processor, ProcessorError

__all__ = ["XarExpander"]


class XarExpander(Processor):
    """Look in the build directory for a pre-existing package."""
    description = __doc__
    input_variables = {
        "archive_path": {
            "required": True,
            "description": "The name of the archive to expand"
        },
        "destination_path": {
            "required": True,
            "description": "The directory to extract to."
        },
    }
    output_variables = {'Extracted': {
        "default": False,
        "description": (
            "False if no built package exists. "
            "True if a package with the same filename, identifier and "
            "version already exists and thus no package needs to be built "
            "(see 'force_pkg_build' input variable."),
    }}

    def xar_expand(self, source_path):
        """Uses xar to expand an archive."""
        # Originally from PkgCreator.py
        extract_path = os.path.join(self.env.get('RECIPE_CACHE_DIR'), 'downloads')
        try:
            xarcmd = ["/usr/bin/xar",
                      "-x",
                      "-C", extract_path,
                      "-f", source_path]
            proc = subprocess.Popen(xarcmd,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            (_, stderr) = proc.communicate()
        except OSError as err:
            raise ProcessorError("xar execution failed with error code %d: %s"
                                 % (err.errno, err.strerror))
        if proc.returncode != 0:
            raise ProcessorError("extraction of %s with xar failed: %s"
                                 % (source_path, stderr))

    def make_extract(self, source_path):
        """Uses xar to expand an archive."""
        # Originally from PkgCreator.py
        try:
            xarcmd = ["/bin/mkdir", '-p', source_path]
            proc = subprocess.Popen(xarcmd,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            (_, stderr) = proc.communicate()
        except OSError as err:
            raise ProcessorError("xar execution failed with error code %d: %s"
                                 % (err.errno, err.strerror))
        if proc.returncode != 0:
            raise ProcessorError("extraction of %s with xar failed: %s"
                                 % (source_path, stderr))

    def mv_file(self, source_path):
        '''Uses xar to expand an archive.'''
        # Originally from PkgCreator.py
        source = os.path.join(self.env.get('RECIPE_CACHE_DIR'), 'downloads/Content')
        dest = os.path.join(source_path, 'Content.gz')
        try:
            xarcmd = ["/bin/mv",
                      source,
                      dest]
            proc = subprocess.Popen(xarcmd,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            (_, stderr) = proc.communicate()
        except OSError as err:
            raise ProcessorError("xar execution failed with error code %d: %s"
                                 % (err.errno, err.strerror))
        if proc.returncode != 0:
            raise ProcessorError("extraction of %s with xar failed: %s"
                                 % (source_path, stderr))

    def gunzip_expand(self, source_path):
        """Use gunzip to extract"""
        # Originally from PkgCreator.py
        gzip_file = os.path.join(source_path, 'Content.gz')
        cpio_file = os.path.join(source_path, 'Content.cpio')
        try:
            xarcmd = ["/usr/bin/gunzip",
                      "-c", gzip_file]
            with open(cpio_file, "w+") as f:
                proc = subprocess.Popen(xarcmd,
                                        stdout=f,
                                        stderr=subprocess.PIPE)
            (_, stderr) = proc.communicate()
        except OSError as err:
            raise ProcessorError("gunzip execution failed with error code %d: %s"
                                 % (err.errno, err.strerror))
        if proc.returncode != 0:
            raise ProcessorError("extraction of %s with xar failed: %s"
                                 % (source_path, stderr))

    def cpio_expand(self, source_path):
        '''Use Cpio to extract'''
        # Originally from PkgCreator.py
        cpio_file = os.path.join(source_path, 'Content.cpio')
        os.chdir(source_path)

        try:
            xarcmd = ["/usr/bin/cpio",
                      "-d", "-i",
                      "-F", cpio_file]
            proc = subprocess.Popen(xarcmd,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            (_, stderr) = proc.communicate()
        except OSError as err:
            raise ProcessorError("xar execution failed with error code %d: %s"
                                 % (err.errno, err.strerror))
        if proc.returncode != 0:
            raise ProcessorError("extraction of %s with xar failed: %s"
                                 % (source_path, stderr))

    def cleanup(self, source_path, path2):
        """Uses xar to expand an archive."""
        # Originally from PkgCreator.py
        gz_file = os.path.join(path2, 'Content.gz')
        Metadata_file = os.path.join(self.env.get('RECIPE_CACHE_DIR'), 'downloads/Metadata')
        cpio_file = os.path.join(path2, 'Content.cpio')
        os.remove(gz_file)
        os.remove(Metadata_file)
        os.remove(cpio_file)

    def main(self):
        """Look for an already built package."""
        self.xar_expand(self.env['archive_path'])
        self.make_extract(self.env['destination_path'])
        self.mv_file(self.env['destination_path'])
        self.gunzip_expand(self.env['destination_path'])
        self.cpio_expand(self.env['destination_path'])
        self.cleanup(self.env['archive_path'],self.env['destination_path'])


if __name__ == '__main__':
    PROCESSOR = XarExpander()
    PROCESSOR.execute_shell()
