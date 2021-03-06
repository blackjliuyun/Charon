import requests
from lib.scheduler.check200or404 import check_200_or_404

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
}


def poc(url):
    url1 = "%s/invoker/JMXInvokerServlet" % url
    result = "目标Jboss可能存在JAVA反序列化漏洞CVE-2007-1036/CVE-2012-0874/CVE-2013-4810/CVE-2017-7501 : %s" % url1
    timeout = 5
    try:
        req = requests.head(url1, headers=headers, timeout=timeout)
        if (req.status_code == 500 or (req.status_code == 200 and check_200_or_404(url1))) and (
                'JBoss'.lower() in str(req.headers).lower() or 'Apache-Coyote/1.1'.lower() in str(req.headers).lower()):
            return result
    except:
        pass


if __name__ == "__main__":
    a = poc('http://192.168.106.130:8080')
    print(a)
