import re


rgx = re.compile(r'^\d{1,3}(\,\d{3})*$')
print(rgx.search('1,000,000').group(0))
