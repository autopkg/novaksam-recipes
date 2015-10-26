#!/usr/bin/env python
#
# Copyright 2015 Sam Novak
#

import os
import errno
import shutil

import FoundationPlist

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
    

