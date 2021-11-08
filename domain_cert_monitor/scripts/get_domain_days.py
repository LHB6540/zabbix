from get_expired_time import get_domain_days
import json


tmp_path='/tmp/domain_info.tmp'
domain_list_path = 'domain_list.json'


domains_info = {"data":[]}
with open(domain_list_path) as f:
    domains = f.read()
domains = json.loads(domains)['data']


for domain in domains:
        print(domain["domain"])
        date = get_domain_days(domain['domain'],(domain.get('port') or 443))
        domains_info["data"].append({
            "{#day}": date,
            "{#NAME}": domain["domain"]
         })

with open(tmp_path,'w'):
    f = open(tmp_path,'w')
    f.write(json.dumps(domains_info))