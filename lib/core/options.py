import sys
import os
from lib.core.data import conf, paths, th
from lib.core.enums import TARGET_MODE_STATUS, ENGINE_MODE_STATUS, SCRIPT_ALL_LIST
from lib.core.console_color import PrintConsole


def initOptions(args):
    # checkShow(args)
    EngineRegister(args)
    ScriptRegister(args)
    TargetRegister(args)
    # ApiRegister(args)
    Output(args)


def checkShow(args):
    pass


def EngineRegister(args):
    thread_num = args.thread_num
    conf.ENGINE = ENGINE_MODE_STATUS.THREAD
    if 0 < thread_num < 501:
        th.THREADS_NUM = conf.THREADS_NUM = thread_num
    else:
        msg = 'Invalid input in [-t], range: 1 to 500'
        sys.exit(PrintConsole(msg, 'error'))


def ScriptRegister(args):
    input_path = args.script_name
    input_all = args.script_all
    conf.MODULE_USE = []
    poc_list = []
    poc_path_list = []
    # handle input: nothing
    if not (input_path or input_all):
        msg = 'Use -s to load script. Example: [-s spider] '
        sys.exit(PrintConsole(msg, 'error'))

    if input_path:
        for poc_path in input_path:
            if not poc_path.endswith('.py'):
                poc_path += '.py'
            a = poc_path.split("_")[0]
            _path = os.path.abspath(os.path.join(paths.POC_PATH, a, poc_path))
            poc_list.append(poc_path)
            poc_path_list.append(_path)
            if os.path.isfile(_path):
                conf.MODULE_NAME = poc_list
                conf.MODULE_FILE_PATH = poc_path_list
            else:
                msg = 'Script %s not exist. ' % poc_path
                sys.exit(PrintConsole(msg, 'error'))
        conf.MODULE_USE.append(conf.MODULE_NAME)
    if input_all:
        for poc_path in SCRIPT_ALL_LIST[input_all]:
            if not poc_path.endswith('.py'):
                poc_path += '.py'
            a = poc_path.split("_")[0]
            _path = os.path.abspath(os.path.join(paths.POC_PATH, a, poc_path))
            poc_list.append(poc_path)
            poc_path_list.append(_path)
            if os.path.isfile(_path):
                conf.MODULE_NAME = poc_list
                conf.MODULE_FILE_PATH = poc_path_list
            else:
                msg = 'Script %s not exist. ' % poc_path
                sys.exit(PrintConsole(msg, 'error'))
        conf.MODULE_USE.append(conf.MODULE_NAME)


def TargetRegister(args):
    input_url = args.target_url
    input_file = args.target_file
    if not (input_url or input_file):
        msg = 'Use -u/-f to load target. Example: [-u/-f http://vuln.com or vuln.txt] '
        sys.exit(PrintConsole(msg, 'error'))
    if input_url:
        conf.TARGET_MODE = TARGET_MODE_STATUS.SINGLE
        conf.INPUT_TARGET_URL = input_url
    if input_file:
        conf.TARGET_MODE = TARGET_MODE_STATUS.FILE
        conf.INPUT_FILE_PATH = input_file


def ApiRegister(args):
    pass


def Output(args):
    pass