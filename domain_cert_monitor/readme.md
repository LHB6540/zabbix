# 脚本说明
脚本1 get_expired_time.py：  
 
获取指定域名、证书的剩余时间    

脚本2 get_domain_day.py：    

借助 get_expired_time.py 获取指定域名列表的所有到期时间并生成 Zabbix 自动发现格式的数据    

脚本3 get_cert_day.py：    

借助 get_expired_time.py 获取指定目录下所有证书文件的到期时间并生成 Zabbix 自动发现格式的数据   

脚本4 get_signal_cert.py：    

借助 get_cert_day.py 生成的数据获取单个证书的剩余有效时间   

脚本5 get_signal_cert.py：   

借助 get_domain_day.py 生成的数据获取单个域名使用的证书的剩余有效时间   
# 如何使用
1、在监控机器上下载 zabbix/domain_cert 的全部内容    

2、将 scripts 存放在一个目录中，当前代码假设 scripts 中的文件存放在 /etc/zabbix/shell/domain_cert ,如果存放在其他目录，请修改定时任务、zabbix-agentd.d 中的相关路径      
   修改 domain_list.json 的域名列表为自己想要监控的域名    
   在 /etc/zabbix/shell/certs 中存放要监控的证书公钥文件，如果要修改为其他目录，请修改 get_domain_day.py 中的 path 变量   
   get_signal_cert.py 、 get_signal_domain.py 将在单个监控项取值时使用，默认的取值相关文件路径位于 /tmp 目录下，如需修改，请修改 get_cert_day.py 、 get_domain_day.py   
   
3、将 zabbix-agentd.d 中的conf文件存放在 zabbix-agent 配置文件目录，通常这个目录为 /etc/zabbix/zabbix-agentd.d/ ，重启 zabbix-agent     

4、按照定时任务中的 crontab 添加定时任务     

5、在 Zabbix Server 的配置-模版中导入模版    

6、对监控机器关联两个模版

