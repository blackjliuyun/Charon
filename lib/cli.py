#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
from lib.core.set_something import banner, set_paths
from lib.core.console_color import PrintConsole
from lib.core.data import cmdLineOptions
from lib.core.options import initOptions
from lib.scheduler.loader import loadModule, loadPayloads
from lib.parse.cmd_parse import cmd_line_parser
from lib.scheduler.engine import run


def module_path():
    """
    This will get us the program's directory
    """
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def check_environment():
    try:
        os.path.isdir(module_path())
    except Exception:
        err_msg = "your system does not properly handle non-ASCII paths. "
        err_msg += "Please move the pocsuite's directory to the other location"
        PrintConsole(err_msg, 'error')
        raise SystemExit


def main():
    """
    @function Main function of pocsuite when running from command line.
    """

    check_environment()
    set_paths(module_path())

    try:
        banner()
        # print(cmd_line_parser())
        cmdLineOptions.update(cmd_line_parser())
        initOptions(cmdLineOptions)

    except:
        pass
    try:
        loadModule()
        loadPayloads()
    except AttributeError:
        exit()
    run()


if __name__ == "__main__":
    main()
