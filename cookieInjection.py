import json
class cookieInjection:
   @classmethod
   def Injection(self,driver):
                #cookie绝对路径
    with open("D:\Python code\myobj\Boss.json", "r") as f:
        jsonCookies=json.loads(f.read())
    i=0
    for cookie in jsonCookies:
        i = 1
        if(i<1):
            driver.add_cookie({
            'domain': cookie['domain'],
            'expiry': cookie['expiry'],
            'httpOnly': cookie['httpOnly'],
            'name': cookie['name'],
            'path': cookie['path'],
            'secure': cookie['secure'],
            'value': cookie['value']
            })
        else:
            driver.add_cookie({
                'domain': cookie['domain'],
                'httpOnly': cookie['httpOnly'],
                'name': cookie['name'],
                'path': cookie['path'],
                'secure': cookie['secure'],
                'value': cookie['value']
            })
           pip selenium
