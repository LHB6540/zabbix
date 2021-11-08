import OpenSSL
import json
import datetime
import sys
import os
from get_expired_time import get_cert_from_file


path = "/etc/zabbix/shell/certs" #文件夹目录
tmp_path = '/tmp/certt_info.txt'
files= os.listdir(path) #得到文件夹下的所有文件名称
ssl_info = {"data":[]}

today = datetime.datetime.today()
for file in files: #遍历文件夹
     if not os.path.isdir(file): 
        cert_date=None
        try: 
            cert_date=get_cert_from_file(path+"/"+file)
        except Exception: 
            pass
        if not cert_date:
            cert_date = 10000
        else:
            day = (cert_date-today).days
            ssl_info["data"].append({"{#FILE}":file,"{#day}":day})

ssl_info=json.dumps(ssl_info,ensure_ascii=False)
with open(tmp_path,'w') as f:
    f.write(ssl_info)