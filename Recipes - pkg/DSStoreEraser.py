#!/usr/bin/env python
#
# Copyright 2015 Sam Novak
#

import os
import errno
import shutil
import re
import FoundationPlist

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
	inputfile = open(self.env["file_path"],'r')
	temp = (re.sub("(.*?)DS_Store","",inputfile.read()))
	outputfile = open(self.env["file_path"],'w')
	outputfile.write(temp)
	inputfile.close()
	outputfile.close()

        


if __name__ == '__main__':
    processor = DSStoreEraser()
    processor.execute_shell()
    

