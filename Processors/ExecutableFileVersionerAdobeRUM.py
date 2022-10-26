#!/usr/local/autopkg/python

from __future__ import absolute_import

import os.path
import subprocess
import re

from autopkglib import Processor, ProcessorError

__all__ = ["ExecutableFileVersioner"]

class ExecutableFileVersionerAdobeRUM(Processor):
    description = ("Gets the version of an executable file collected by FileFinder. ")
    input_variables = {
        "found_filename": {
            "required": True,
            "description": (
                "Full path to the executable file collected "
                "by FileFinder. "
            ),
        },
        "interpreter_path": {
            "required": False,
            "default": "/usr/bin/python",
            "description": (
                "Full path to the interpreter to call the executable "
                "file, if needed. "
            ),
        },
        "version_argument": {
            "required": True,
            "description": (
                "Argument passed to executable file to collect "
                "its version. "
            ),
        }
    }
    output_variables = {
        "version": { "description": "The executable file version" }
    }

    __doc__ = description

    def main(self):
        if not os.path.exists(self.env['found_filename']):
            raise ProcessorError("\nCould not find executable at %s" % (self.env['found_filename']))
        else: 
            self.output("Found executable at %s" % self.env['found_filename'])

        try:
            chmod = subprocess.check_output([ '/bin/chmod', '+x', self.env['found_filename']])
            strings = subprocess.check_output(([ '/usr/bin/strings', self.env['found_filename']]),encoding='utf-8')
            cmd = re.search('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', strings, re.MULTILINE)
            #cmd = subprocess.Popen(('/usr/bin/grep', '-e', '-m1', "string\>[0-9]+\.[0-9]+\.[0-9]\.[0-9]"), stdin=strings.stdout)
            #strings.wait()
            #strings.stdout.close()
            #cmd.communicate()
            #cmd = subprocess.check_output([ self.env['found_filename'], self.env['version_argument']], stderr=subprocess.STDOUT)
            # Get version and remove offending new line at the end
            self.env['version'] = cmd[0]
            self.output("Version: %s" % self.env['version'])
        #except subprocess.CalledProcessError:
            #self.env['version'] = cmd.rstrip('\n')
            #self.output("Version: %s" % self.env['version'])
        except OSError:
            raise ProcessorError("Can't find %s" % (self.env['found_filename']))
            

if __name__ == '__main__':
    processor = ExecutableFileVersioner()
    processor.execute_shell()
