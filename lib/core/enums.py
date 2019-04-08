#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me


SCRIPT_ALL_LIST = {
    'thinkphp5_all': ['thinkphp5_rce', 'thinkphp5_5010rce', 'thinkphp5_5023rce', 'thinkphp5_5152rce'],
    'struts2_all': ['struts2_003', 'struts2_005', 'struts2_008', 'struts2_009', 'struts2_013', 'struts2_015',
                    'struts2_016', 'struts2_019', 'struts2_032', 'struts2_033', 'struts2_037', 'struts2_045',
                    'struts2_046', 'struts2_048', 'struts2_048_1', 'struts2_052', 'struts2_053', 'struts2_dev'],
    'weblogic_all': ['weblogic_4852', 'weblogic_0638', 'weblogic_3510', 'weblogic_3248', 'weblogic_3506',
                     'weblogic_2628', 'weblogic_2893', 'weblogic_weak', 'weblogic_ssrf'],
    'joomla_all': ['jooml_videoflow_sqli', 'joomla_registrationpro_sqli', 'joomla_videogallerylite_sqli']

}


class CONTENT_STATUS:
    IN_PROGRESS = 0
    COMPLETE = 1


class POC_RESULT_STATUS:
    FAIL = 0
    SUCCESS = 1
    RETRAY = 2


class API_MODE_NAME:
    ZOOMEYE = 'ZoomEye'
    SHODAN = 'Shodan'
    GOOGLE = 'Google'
    FOFA = 'Fofa'


class TARGET_MODE_STATUS:
    FILE = 9
    SINGLE = 8
    IPMASK = 7
    RANGE = 6
    API = 5


class ENGINE_MODE_STATUS:
    THREAD = 9
    GEVENT = 8


class PROXY_TYPE:  # keep same with SocksiPy(import socks)
    PROXY_TYPE_SOCKS4 = SOCKS4 = 1
    PROXY_TYPE_SOCKS5 = SOCKS5 = 2
    PROXY_TYPE_HTTP = HTTP = 3
    PROXY_TYPE_HTTP_NO_TUNNEL = 4
