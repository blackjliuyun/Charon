import requests
from lib.scheduler.check200or404 import check_200_or_404

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
}


def poc(url):
    url1 = "%s/admin-console/" % url
    result = "Maybe jBoss vuln CVE-2010-1871 : %s" % url1
    timeout = 5
    try:
        req = requests.head(url1, headers=headers, timeout=timeout)
        if (req.status_code == 500 or (req.status_code == 200 and check_200_or_404(url1))) and (
                    'JBoss'.lower() in str(req.headers).lower() or 'Apache-Coyote/1.1'.lower() in str(req.headers).lower()):
            return result
    except:
        pass


if __name__ == "__main__":
    a = poc('http://60.174.64.241:8090')
    print(a)
