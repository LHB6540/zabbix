import sys
import json


tmp_path = '/tmp/domain_info.tmp'

name = sys.argv[1]
day = 10000

with open(tmp_path) as f:
    domain_info = f.read()


domain_data= json.loads(domain_info)
for i in domain_data["data"]:
        if i['{#NAME}'] == name:
                day = i['{#day}']
                break
print(day)