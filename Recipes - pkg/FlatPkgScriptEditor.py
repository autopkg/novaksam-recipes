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


class FlatPkgScriptEditor(Processor):
    description = """Modifies scripts, and other files, allowing single line modification."""

    input_variables = {
        "pathname": {
            "required": True,
            "description": "Path to where the file you want to modify is"
        },
        "text_to_replace": {
            "required": True,
            "description": """The text to search find."""
        },
        "replacement_text": {
            "required": False,
            "description": """The text to replace the found text with"""
        }
    }
    
    output_variables = {
    }
    
    __doc__ = description


    
    def main(self):
        
        os.chmod(self.env["pathname"],0644)
        f = open(self.env["pathname"],'r')
        filedata = f.read()
        f.close()
        
        newdata = filedata.replace(self.env["text_to_replace"],self.env["replacement_text"])
        
        f=open(self.env["pathname"],'w')
        f.write(newdata)
        f.close()
        os.chmod(self.env["pathname"],0744)
        


if __name__ == '__main__':
    processor = FlatPkgScriptEditor()
    processor.execute_shell()
    

