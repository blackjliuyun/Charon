from lib.core.data import conf, th
from lib.core.console_color import PrintConsole
from lib.core.enums import ENGINE_MODE_STATUS, POC_RESULT_STATUS
import os
import threading
import time
import sys
import traceback
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def initEngine():
    th.thread_mode = True if conf.ENGINE is ENGINE_MODE_STATUS.THREAD else False
    th.f_flag = True
    th.s_flag = True
    th.thread_count = th.threads_num = th.THREADS_NUM
    th.single_mode = False
    th.scan_count = th.found_count = 0
    th.is_continue = True
    th.found_single = False
    th.start_time = time.time()
    setThreadLock()
    msg = '设置的线程数为: %d' % th.threads_num
    PrintConsole(msg, 'info')


def singleMode():
    th.is_continue = False
    th.found_single = True


def scan():
    while 1:
        if th.thread_mode: th.load_lock.acquire()
        if th.queue.qsize() > 0 and th.is_continue:
            module = th.queue.get(timeout=1.0)
            payload = str(module["sub"])
            module_obj = module["poc"]
            if th.thread_mode: th.load_lock.release()
        else:
            if th.thread_mode: th.load_lock.release()
            break
        try:
            # POC在执行时报错如果不被处理，线程框架会停止并退出
            # sys.stdout.write('\r' + payload + '\n\r')
            status = module_obj.poc(payload)
            resultHandler(status, module)
        # except KeyboardInterrupt:
        #     th.is_continue = False
        #     raise KeyboardInterrupt
        except:
            th.errmsg = traceback.format_exc()
            th.is_continue = False
        changeScanCount(1)
        if th.s_flag:
            printProgress()
    if th.s_flag:
        printProgress()

    changeThreadCount(-1)


def run():
    initEngine()
    if conf.ENGINE is ENGINE_MODE_STATUS.THREAD:
        for i in range(th.threads_num):
            t = threading.Thread(target=scan, name=str(i))
            t.setDaemon(True)
            t.start()
        while 1:
            if th.thread_count > 0 and th.is_continue:
                time.sleep(0.01)
            else:
                break
    sys.stdout.write('\n')
    if 'errmsg' in th:
        # pass
        PrintConsole(th.errmsg, 'error')
    if th.found_single:
        msg = "[single-mode] found!"
        PrintConsole(msg, 'info')


def resultHandler(status, payload):
    def printScrren(msg):
        i = th.found_count
        if th.s_flag:
            printMessage(msg)
        if th.s_flag:
            output2file(i, msg)
        if th.single_mode:
            singleMode()

    if not status or status is POC_RESULT_STATUS.FAIL:
        return
    elif status is POC_RESULT_STATUS.RETRAY:
        changeScanCount(-1)
        th.queue.put(payload)
        return
    elif status is True or status is POC_RESULT_STATUS.SUCCESS:
        msg = "目标存在 " + payload["name"][:-3] + " : " + payload["sub"]
        printScrren(msg)
    else:
        if type(status) == set:
            for x in status:
                printScrren(str(x))
        elif type(status) == list:
            for x in status:
                printScrren(str(x))
        else:
            msg = str(status)
            printScrren(msg)
    changeFoundCount(1)


def setThreadLock():
    if th.thread_mode:
        th.found_count_lock = threading.Lock()
        th.scan_count_lock = threading.Lock()
        th.thread_count_lock = threading.Lock()
        th.file_lock = threading.Lock()
        th.load_lock = threading.Lock()


def changeFoundCount(num):
    if th.thread_mode: th.found_count_lock.acquire()
    th.found_count += num
    if th.thread_mode: th.found_count_lock.release()


def changeScanCount(num):
    if th.thread_mode: th.scan_count_lock.acquire()
    th.scan_count += num
    if th.thread_mode: th.scan_count_lock.release()


def changeThreadCount(num):
    if th.thread_mode: th.thread_count_lock.acquire()
    th.thread_count += num
    if th.thread_mode: th.thread_count_lock.release()


def printMessage(msg):
    sys.stdout.write('\r' + msg + '\n\r')
    # pass


def printProgress():
    msg = '[结果] 发现 %s | 剩余 %s | 探测的 %s 个在 %.2f 秒内' % (
        th.found_count, th.queue.qsize(), th.scan_count, time.time() - th.start_time)
    out = '\r' + ' ' + msg
    sys.stdout.write(out)


#
def output2file(i, msg):
    if th.thread_mode: th.file_lock.acquire()
    file_name = '{0}\output/{1}.{2}'.format(os.getcwd(), "report-" + time.strftime("%Y-%m-%d", time.localtime()),
                                            'html')

    url = msg.split(':')[1]
    if 'http://' not in url:
        url = 'http://' + url
    f = open(file_name, 'a')
    f.write(
        "<style (type='text/css')>a:visited {color: red;}</style>"'&nbsp&nbsp' + str(
            i) + ':&nbsp&nbsp' + "<a href=" + url + "target=_blank>" + msg + "</a>" + '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + "<br>")

    f.close()
    if th.thread_mode: th.file_lock.release()
