from lib.core.config import BANNER
from lib.core.console_color import PrintConsole
from lib.core.data import paths, conf
from lib.core.enums import ENGINE_MODE_STATUS
import os
import sys


def banner():
    PrintConsole(BANNER, 'banner')


def set_paths(root_path):
    """
    Sets absolute paths for project directories and files
    """
    paths.Charon_ROOT_PATH = root_path
    paths.DATA_PATH = os.path.join(paths.Charon_ROOT_PATH, "data")
    paths.POC_PATH = os.path.join(paths.Charon_ROOT_PATH, "poc")
    paths.USER_AGENTS = os.path.join(paths.DATA_PATH, "user-agents.txt")
    paths.WEAK_PASS = os.path.join(paths.DATA_PATH, "pass100.txt")
    paths.LARGE_WEAK_PASS = os.path.join(paths.DATA_PATH, "pass1000.txt")


# def dataToStdout(data, bold=False):
#     """
#     Writes text to the stdout (console) stream
#     """
#     if conf.SCREEN_OUTPUT:
#         if conf.ENGINE is ENGINE_MODE_STATUS.THREAD:
#             PrintConsole._acquireLock()
#
#         message = data
#
#         sys.stdout.write(setColor(message, bold))
#
#         try:
#             sys.stdout.flush()
#         except IOError:
#             pass
#
#         if conf.ENGINE is ENGINE_MODE_STATUS.THREAD:
#             logging._releaseLock()
#     return
