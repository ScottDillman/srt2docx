# -*- coding: utf-8 -*-
"""Script to convert SRT files to DOCX files with tables

Example of end state:
- https://docs.google.com/document/d/1MqnG5MWRbjZBke9ja5CN-rJGijJnWBrRJa6lLOxMvRQ/edit

SRT format docs
- https://en.wikipedia.org/wiki/SubRip

DOCX docs
- https://python-docx.readthedocs.io/en/latest/

Example:

        $ python srt2docx.py

Todo:
    * Option to go directly to google docs
    * Option to combine all files into one docx
    * add recursion option glob.glob('**/*.txt', recursive=True)
    * add better error handling

This script reads settings from a srt2docx_settings.yaml file in the same directory as the
script file. Edit this file to personalize the settings. This only has to be done once.

Generally there is a make file distributed with this script and can be executed as
follows:

    % make setup

otherwise run the following to initialize the environment:

    % python -m venv pyenv
        % source ./pyenv/bin/activate
        % pip install -r requirements.txt

Then activate the environment:

    % activate env with: source ./pyenv/bin/activate

Then in a directory containing the files to be processed run:

$ python srt2docx.py

Output files will have the same name as input files but with the .docx extension.

@Author: Scott Dillman <scott@bitwise.ninja>
@Date: 2024-06-25 22:47
"""

import srt2docx_funcs
import argparse
from loguru import logger
import inspect
import os


## argument parser
parser = argparse.ArgumentParser(
    prog="srt2docx",
    epilog="Please contact scott@bitwise.ninja with problems/issues",
    description="Convert srt files to tables in docx",
)

## update me on major changes
__version__ = "0.1.2"
__contact__ = "scott@bitwise.ninja"
__web__ = "https://dreamcyclesetudios.com"


## main entry point
def main():
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s " + __version__ + " | {} | {}".format(__contact__, __web__),
    )
    parser.parse_args()

    ## do any init we need
    logger.info("Script started: [{}]".format(os.path.realpath(inspect.stack()[0][1])))
    srt2docx_funcs.init(__version__)


if __name__ == "__main__":
    main()
