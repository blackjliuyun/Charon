import importlib.util
import sys
import queue
from lib.core.data import conf, th
from lib.core.enums import TARGET_MODE_STATUS
from lib.core.console_color import PrintConsole


def loadModule():
    conf.MODULE_PLUGIN = dict()
    for _name in conf.MODULE_USE:
        msg = '加载的Payloads: %s' % _name
        PrintConsole(msg, 'info')
        # for name in _name:
        for file_path in conf.MODULE_FILE_PATH:
            name = file_path.split("\\")[-1]
            try:
                spec = importlib.util.spec_from_file_location(name, file_path)
                module_obj = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module_obj)
                for each in ['poc']:
                    if not hasattr(module_obj, each):
                        error_msg = "Can't find essential method:'%s()' in current script，Please modify your script/PoC." % each
                        sys.exit(PrintConsole(error_msg, 'error'))
                    conf.MODULE_PLUGIN[name] = module_obj
            except:
                error_msg = "Your current scipt [%s] caused this exception" % name
                sys.exit(PrintConsole(error_msg, 'error'))


def loadPayloads():
    info_msg = '初始化Payload...'
    PrintConsole(info_msg, 'info')
    th.queue = queue.Queue()
    if conf.TARGET_MODE is TARGET_MODE_STATUS.SINGLE:
        single_target_mode()
    elif conf.TARGET_MODE is TARGET_MODE_STATUS.FILE:
        file_mode()
    # else:
    #     raise ('conf.TARGET_MODE value ERROR.')
    PrintConsole('总数: %s' % str(th.queue.qsize()), 'info')


def single_target_mode():
    # try:
    for name, exp in conf.MODULE_PLUGIN.items():
        module = dict()
        if '://' not in str(conf.INPUT_TARGET_URL):
            conf.INPUT_TARGET_URL = 'http://' + str(conf.INPUT_TARGET_URL)
        module["sub"] = str(conf.INPUT_TARGET_URL)
        module["poc"] = exp
        module["name"] = name
        th.queue.put(module)
    # except:
    #     PrintConsole("检查参数是否输入错误 eg.", 'error')


def file_mode():
    try:
        for line in open(conf.INPUT_FILE_PATH):
            for name, exp in conf.MODULE_PLUGIN.items():
                sub = line.strip()
                if '://' not in sub:
                    sub = 'http://' + sub
                if sub:
                    module = dict()
                    module["sub"] = sub
                    module["name"] = name
                    module["poc"] = exp
                    th.queue.put(module)
    except:
        PrintConsole("检查参数是否输入错误 eg. -f/vuln.txt", 'error')
