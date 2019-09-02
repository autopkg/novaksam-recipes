#!/usr/bin/python
#
# Copyright 2017 Sam Novak
#
# Based on autopkg processors written by Greg Neagle
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
"""See docstring for MinimumOSExtractor class"""

from __future__ import absolute_import

import os.path
import xml.etree.ElementTree as ET

from autopkglib import Processor, ProcessorError

__all__ = ["PackageInfoReader"]



class PackageInfoReader(Processor):
    """Returns the version and identifier from an existing PackageInfo file, located instead of a non-flat pkg file
       """
    description = __doc__

    input_variables = {
        "packageinfo_path": {
            "required": True,
            "description":
                ("File path to a PackageInfo file."),
        },
    }
    output_variables = {
        "pkginfo_version": {
            "description": "version from the PackageInfo file.",
        },
        "bundleid": {
            "description": "BundleID from the PackageInfo file",
        },
    }

    def main(self):
        """Return a version for file at packageinfo_path"""
        packageinfo_path = self.env['packageinfo_path']

        if not os.path.exists(packageinfo_path):
            raise ProcessorError(
                "File '%s' does not exist or could not be read." %
                packageinfo_path)
        try:
            """Import the file as XML"""
            xml_tree = ET.parse(packageinfo_path)
            xml_root = xml_tree.getroot()
            """Get the variables out of the XML"""
            pkginfo_version = xml_root.get('version')
            bundleid = xml_root.get('identifier')
            """Set our variables for the output"""
            self.env["pkginfo_version"] = str(pkginfo_version)
            self.env["bundleid"] = str(bundleid)

        except FoundationPlist.FoundationPlistException as err:
            raise ProcessorError(err)




if __name__ == '__main__':
    PROCESSOR = PackageInfoReader()
    PROCESSOR.execute_shell()
