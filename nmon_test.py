#!/usr/bin/python3
"""
run the following:python3 nmon_test.py -d -x -c -b -t "stat" -i ../tmp_logs/test.nmon -r ./py_nmon_pack/report.config


make sure your .nmon file is in the right location
make sure you have the py_nmon_pack folder in the same directory as is nmon_test.py
in the first run, if report.config does not 
the output will be written into 

look at these arguments you can pass: 
 parser = argparse.ArgumentParser(
            description="nmonParser converts NMON monitor files into time-sorted CSV/Spreadsheets for easier analysis, without the use of the MS Excel Macro. Also included is an option to build an HTML report with graphs, which is configured through report.config.")
        parser.add_argument("-x", "--overwrite", action="store_true",
                            dest="overwrite", help="overwrite existing results (Default: False)")
        parser.add_argument("-d", "--debug", action="store_true",
                            dest="debug", help="debug? (Default: False)")
        parser.add_argument("--force", action="store_true", dest="force",
                            help="force using of config (Default: False)")
        parser.add_argument("-i", "--inputfile", dest="input_file",
                            default="test.nmon", help="Input NMON file")
        parser.add_argument("-o", "--output", dest="outdir", default="./report/",
                            help="Output dir for CSV (Default: ./report/)")
        parser.add_argument("-c", "--csv", action="store_true",
                            dest="outputCSV", help="CSV output? (Default: False)")
        parser.add_argument("-b", "--buildReport", action="store_true",
                            dest="buildReport", help="report output? (Default: False)")
        parser.add_argument("-t", "--reportType", dest="reportType", default="inter",
                            help="Should we be generating a \"stat\" or \"inter\" report (Default: interactive)")
        parser.add_argument("-r", "--reportConfig", dest="confFname", default="./report.config",
                            help="Report config file, if none exists: we will write the default config file out (Default: ./report.config)")
        parser.add_argument("--dygraphLocation", dest="dygraphLoc", default="http://dygraphs.com/1.1.0/dygraph-combined.js",
                            help="Specify local or remote location of dygraphs library. This only applies to the interactive report. (Default: http://dygraphs.com/1.1.0/dygraph-combined.js)")
        parser.add_argument("--defaultConfig", action="store_true",
                            dest="defaultConf", help="Write out a default config file")
        parser.add_argument("-l", "--log", dest="logLevel", default="INFO",
                            help="Logging verbosity, use DEBUG for more output and showing graphs (Default: INFO)")
        args = parser.parse_args(raw_args)
"""


from __future__ import print_function
import os
import sys
from shutil import rmtree
import argparse
import logging as log


from py_nmon_pack.pyNmonParser import pyNmonParser;
from py_nmon_pack.pyNmonPlotter import pyNmonPlotter;
from py_nmon_pack.pyNmonReport import htmlheader, createReport, createInteractiveReport;
from  py_nmon_pack.pyNmonAnalyzer import pyNmonAnalyzer;

if __name__ == "__main__":
    _ = pyNmonAnalyzer(raw_args=sys.argv[1:])