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


@Author: Scott Dillman <scott@bitwise.ninja>
@Date: 2024-06-25 22:47
"""

import uuid
from munch import munchify
import yaml
from loguru import logger
from pathlib import Path
from datetime import datetime
import srt
import pytz
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import inspect
import os


def readFiles(values) -> list:
    """read files from cwd"""
    logger.info("Glob in effect is: [{}]".format(values.settings.filetypes.glob))
    files = list(Path().glob(values.settings.filetypes.glob))
    return files


def buildDocument(values, subs, title, version):
    """build the docx document"""
    document = Document()

    ## add base file name as heading
    document.add_heading(title, 0)

    ## add SRT data in table
    table = document.add_table(rows=1, cols=values.settings.table.cols)
    table.autofit = False
    table.allow_autofit = False

    table.columns[0].width = Inches(0.75)
    table.rows[0].cells[0].width = Inches(0.75)

    table.columns[1].width = Inches(0.75)
    table.rows[0].cells[1].width = Inches(0.75)

    table.columns[2].width = Inches(0.75)
    table.rows[0].cells[2].width = Inches(0.75)

    table.columns[3].width = Inches(5.65)
    table.rows[0].cells[3].width = Inches(5.65)

    ## create table header
    hdr_cells = table.rows[0].cells
    count = 0
    for h in values.settings.table.headers:
        hdr_cells[count].text = h
        count = count + 1


    ## iterate over the subs and add data to table
    for item in subs:
        row_cells = table.add_row().cells

        ## drop microseconds
        row_cells[0].text = str(item.start).split(".")[0]
        row_cells[1].text = str(item.end).split(".")[0]

        row_cells[2].text = str((item.end - item.start)).split(".")[0]

        row_cells[3].text = "{}".format(item.content)

    ## set margins
    document.sections[0].left_margin = Inches(values.settings.layout.margin_left)
    document.sections[0].right_margin = Inches(values.settings.layout.margin_right)

    ## add core properties
    cprops = document.core_properties

    ## add basic document properties from the config yaml
    cprops.author = values.settings.meta.author
    cprops.category = values.settings.meta.category
    cprops.comments = values.settings.meta.comments
    cprops.content_status = values.settings.meta.content_status
    cprops.keywords = values.settings.meta.keywords
    cprops.language = values.settings.meta.language
    cprops.subject = values.settings.meta.subject
    cprops.version = values.settings.meta.version
    cprops.last_modified_by = values.settings.meta.author

    ## UTC is expected, localization happens on the client
    tz = pytz.timezone("UTC")
    cprops.created = datetime.now(tz)
    cprops.modified = datetime.now(tz)

    ## assign a UUID to make this document unique and to tag it with eh str2docx version
    ## we put the versioon here in case we need to debug a broken file
    cprops.identifier = "v{}-{}".format(version, str(uuid.uuid4()))
    logger.info("Document unique id: [{}]", cprops.identifier)

    ## let's add a fun footer
    if values.settings.footer.show:
        section = document.sections[0]
        section.footer_distance = Inches(0.2)
        footer = section.footer
        footer_para = footer.paragraphs[0]
        logo_run = footer_para.add_run()

        ## if you want other watermarks put them in the assets directory
        ## because that is where we look for this file
        p = os.path.join(
            os.path.dirname(os.path.realpath(inspect.stack()[0][1])), "assets"
        )
        logo_run.add_picture(
            os.path.join(p, values.settings.footer.watermark),
            width=Inches(values.settings.footer.width_in),
        )
        footer_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    ## save the doc out using the base name from read file
    logger.info("Saving: [{}.docx]".format(title))
    document.save("{}.docx".format(title))


def processFiles(values, files: list, version: str):
    """transform files"""
    ## iterate over file list
    for i in files:
        logger.info("Processing: [{}]".format(i))
        subs = []
        ## open the file for reading
        with open(i) as f:
            ## parse the srt file
            subs = list(srt.parse(f))
            ## build doc
            buildDocument(values, subs, Path(i).stem, version)


def init(version: str) -> dict:
    """Put any setup that needs to be done here"""

    ## so this beast gets the path to the settings file as an absolute path
    ## to the running script
    p = os.path.join(
        os.path.dirname(os.path.realpath(inspect.stack()[0][1])),
        "srt2docx_settings.yaml",
    )

    ## load settings
    values = munchify(yaml.safe_load(open(p)))

    ## do the work
    files = readFiles(values)
    processFiles(values, files, version)

    return values
